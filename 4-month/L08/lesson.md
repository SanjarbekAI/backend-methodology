# L41 — PostgreSQL + Python (psycopg2)

## Why this matters
Every SQL skill you have built means nothing until you can use it from Python. `psycopg2` is the industry-standard PostgreSQL adapter for Python — it powers Django's database layer, SQLAlchemy's PostgreSQL backend, and countless production systems. This lesson bridges the gap between "SQL in the terminal" and "a real Python application that reads and writes a database."

---

## Topics

## Installing psycopg2 & connecting

```bash
# Activate your virtual environment first
python -m venv venv
source venv/bin/activate          # Linux/macOS
venv\Scripts\activate             # Windows

# Install psycopg2
pip install psycopg2-binary       # binary version — no compilation needed
pip freeze > requirements.txt
```

```python
import psycopg2

# Connect to a PostgreSQL database
conn = psycopg2.connect(
    host="localhost",        # database server address
    port=5432,               # default PostgreSQL port
    database="shop_db",      # database name
    user="shop_user",        # PostgreSQL user
    password="securepass123" # password
)

# Always close the connection when done
conn.close()
```

> ⚠️ **Common mistake:** Hardcoding credentials directly in the script. If you commit this to Git, your database password is exposed. Always use environment variables or a `.env` file loaded with `python-dotenv`.

```python
import os
from dotenv import load_dotenv

load_dotenv()   # reads .env file into environment variables

conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", 5432),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
```

```
# .env file (never commit this to Git)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=shop_db
DB_USER=shop_user
DB_PASSWORD=securepass123
```

---

## The cursor — executing SQL

```python
import psycopg2

conn = psycopg2.connect(database="shop_db", user="shop_user", password="securepass123")

# A cursor is the object that sends SQL to the database
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT id, name, price FROM products WHERE is_active = TRUE")

# Fetch results
all_rows = cursor.fetchall()        # list of tuples: [(1, 'Laptop', 4500000), ...]
one_row  = cursor.fetchone()        # single tuple or None
some_rows = cursor.fetchmany(10)    # list of up to 10 tuples

# Iterate directly (memory-efficient for large results)
cursor.execute("SELECT * FROM products")
for row in cursor:
    print(row)   # each row is a tuple

# Always close cursor and connection
cursor.close()
conn.close()
```

---

## Parameterized queries — THE most important pattern
Never concatenate user input into SQL strings. That is the #1 cause of SQL injection — one of the most critical security vulnerabilities.

```python
# NEVER DO THIS — SQL INJECTION VULNERABILITY
user_input = "'; DROP TABLE products; --"
cursor.execute(f"SELECT * FROM products WHERE name = '{user_input}'")  # DANGEROUS

# ALWAYS DO THIS — parameterized query (psycopg2 handles escaping)
cursor.execute(
    "SELECT * FROM products WHERE name = %s AND category = %s",
    (product_name, category)      # second argument: tuple of values
)

# INSERT with parameters
cursor.execute(
    """
    INSERT INTO customers (full_name, email, phone)
    VALUES (%s, %s, %s)
    RETURNING id
    """,
    ("Nilufar Karimova", "nilufar@mail.com", "+998901234567")
)
new_id = cursor.fetchone()[0]      # get the returned id
print(f"New customer created with id: {new_id}")

# Always commit after INSERT/UPDATE/DELETE
conn.commit()
```

> ⚠️ **Common mistake:** Using Python string formatting (`%` or `f-string`) to build SQL queries with user input. This is SQL injection and is the most common serious security vulnerability in web applications. Always use `%s` placeholders and let psycopg2 handle escaping.

---

## Context manager pattern — the professional way

```python
import psycopg2
from contextlib import contextmanager

# Using with statement — connection auto-closes even if an exception occurs
with psycopg2.connect(
    host="localhost", database="shop_db",
    user="shop_user", password="secret"
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM products")
        count = cursor.fetchone()[0]
        print(f"Total products: {count}")
# conn and cursor are automatically closed here

# Reusable connection factory
@contextmanager
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    try:
        yield conn
        conn.commit()             # commit if no exception
    except Exception:
        conn.rollback()           # rollback on any error
        raise
    finally:
        conn.close()              # always close

# Usage:
with get_db_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Widget", 5000))
```

---

## DictCursor — rows as dictionaries
By default, psycopg2 returns rows as **tuples**. `DictCursor` returns them as **dict-like objects** — much easier to work with.

```python
import psycopg2
import psycopg2.extras

with psycopg2.connect(database="shop_db", user="shop_user", password="secret") as conn:
    # Use DictCursor for dict-style row access
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT id, name, price, stock FROM products WHERE is_active = TRUE")
        products = cur.fetchall()

        for p in products:
            # Access by column name instead of index
            print(f"{p['name']}: {p['price']:,.0f} sum | Stock: {p['stock']}")
            # p['name'] is cleaner than p[1]

# RealDictCursor: returns actual Python dicts (serializable to JSON)
with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cur.fetchone()
    # product is now a real dict: {"id": 1, "name": "Laptop", ...}
    import json
    print(json.dumps(dict(product), default=str))  # serializable!
```

---

## Building a database layer — Repository pattern

```python
# db/repository.py
import psycopg2
import psycopg2.extras
import os
from typing import Optional

class ProductRepository:
    """Handles all database operations for the products table."""

    def __init__(self, conn: psycopg2.extensions.connection) -> None:
        self.conn = conn       # receive connection from outside (dependency injection)

    def get_all(self, active_only: bool = True) -> list[dict]:
        """Return all products, optionally only active ones."""
        query = "SELECT id, name, price, stock FROM products"
        params = ()
        if active_only:
            query += " WHERE is_active = TRUE"
        query += " ORDER BY name"
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, params)
            return [dict(row) for row in cur.fetchall()]

    def get_by_id(self, product_id: int) -> Optional[dict]:
        """Return one product by id, or None if not found."""
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                "SELECT * FROM products WHERE id = %s",
                (product_id,)
            )
            row = cur.fetchone()
            return dict(row) if row else None

    def create(self, name: str, price: float, category: str, stock: int = 0) -> int:
        """Insert a new product and return its new id."""
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO products (name, price, category, stock)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                """,
                (name, price, category, stock)
            )
            new_id = cur.fetchone()[0]
            self.conn.commit()
            return new_id

    def update_stock(self, product_id: int, new_stock: int) -> bool:
        """Update stock for a product. Returns True if row was found."""
        with self.conn.cursor() as cur:
            cur.execute(
                "UPDATE products SET stock = %s WHERE id = %s RETURNING id",
                (new_stock, product_id)
            )
            updated = cur.fetchone()
            self.conn.commit()
            return updated is not None

    def delete(self, product_id: int) -> bool:
        """Delete a product. Returns True if row existed."""
        with self.conn.cursor() as cur:
            cur.execute(
                "DELETE FROM products WHERE id = %s RETURNING id",
                (product_id,)
            )
            deleted = cur.fetchone()
            self.conn.commit()
            return deleted is not None
```

---

## Error handling with psycopg2

```python
import psycopg2
from psycopg2 import errors as pg_errors

try:
    with psycopg2.connect(database="shop_db", user="shop_user", password="secret") as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO customers (email) VALUES (%s)",
                ("existing@mail.com",)    # duplicate email
            )
            conn.commit()

except pg_errors.UniqueViolation:
    print("Error: This email is already registered.")
    conn.rollback()

except pg_errors.ForeignKeyViolation:
    print("Error: Referenced record does not exist.")
    conn.rollback()

except pg_errors.NotNullViolation:
    print("Error: A required field is missing.")
    conn.rollback()

except psycopg2.OperationalError as e:
    print(f"Cannot connect to database: {e}")

except psycopg2.DatabaseError as e:
    print(f"Database error: {e}")
    conn.rollback()
```

---

## Quick reference

| Pattern | Code | Notes |
|---|---|---|
| Connect | `psycopg2.connect(host=, database=, user=, password=)` | Use env vars for credentials |
| Cursor | `conn.cursor()` | Needed to execute SQL |
| Execute query | `cur.execute("SELECT...", (param,))` | Always use `%s` for params |
| Fetch all | `cur.fetchall()` | List of tuples |
| Fetch one | `cur.fetchone()` | One tuple or None |
| Dict rows | `cursor_factory=RealDictCursor` | Access by column name |
| Commit | `conn.commit()` | Required after INSERT/UPDATE/DELETE |
| Rollback | `conn.rollback()` | Undo uncommitted changes on error |
| Context mgr | `with conn:` / `with cur:` | Auto-close and commit/rollback |
| SQL injection | Never use f-strings for SQL! | Use `%s` placeholders only |

---

## Task list
1. First connection — the database ping tool
2. Product manager CLI — full CRUD from the terminal
3. Customer search tool — parameterized queries
4. Repository pattern — a clean database layer
5. Terminal app — inventory manager with error handling

---

## SQL LeetCode
- [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) — 🟠 Medium
- [Rank Scores](https://leetcode.com/problems/rank-scores/) — 🟠 Medium

