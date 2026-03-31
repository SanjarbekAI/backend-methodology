# L36 — Relational Databases & PostgreSQL Intro

## Why this matters
Every application that stores data — Instagram, your bank, an e-commerce site — uses a database. Python scripts that only save to files stop working the moment two users try to access the data simultaneously. PostgreSQL is the most advanced open-source relational database in the world, used by companies like Instagram, Spotify, and Twitch. Learning it is the single biggest leap from "writing scripts" to "building real systems."

---

## Topics

## What is a relational database?
A **relational database** stores data in **tables** — like spreadsheets, but with strict structure, relationships between tables, and the ability to query millions of rows in milliseconds.

- **Table:** a named collection of rows (like a Python list of dicts, but permanent)
- **Row (record):** one item in a table
- **Column (field):** one attribute of every row
- **Primary Key:** a unique identifier for each row — no two rows can share it
- **Foreign Key:** a column that references the primary key of another table — this is what creates *relationships*

```
Table: customers                    Table: orders
┌────┬──────────┬──────────────┐    ┌────┬─────────────┬──────────┬────────┐
│ id │ name     │ email        │    │ id │ customer_id │ product  │ amount │
├────┼──────────┼──────────────┤    ├────┼─────────────┼──────────┼────────┤
│  1 │ Nilufar  │ n@mail.com   │    │  1 │           1 │ Laptop   │ 850000 │
│  2 │ Sardor   │ s@mail.com   │    │  2 │           1 │ Mouse    │  45000 │
│  3 │ Malika   │ m@mail.com   │    │  3 │           2 │ Keyboard │  95000 │
└────┴──────────┴──────────────┘    └────┴─────────────┴──────────┴────────┘
              ↑                                   ↑
              └───────── orders.customer_id references customers.id
```

> 💡 **Analogy:** Think of a relational database as a collection of Excel sheets where certain cells in one sheet can *point* to rows in another sheet — and the database enforces that those pointers are always valid.

---

## Installing & connecting to PostgreSQL
```bash
# Install PostgreSQL (Ubuntu/Debian)
sudo apt install postgresql postgresql-contrib

# Install PostgreSQL (macOS with Homebrew)
brew install postgresql@15
brew services start postgresql@15

# Install PostgreSQL (Windows)
# Download from: https://www.postgresql.org/download/windows/
# The installer includes pgAdmin and psql

# Connect using the psql terminal client
psql -U postgres                    # connect as the postgres superuser
psql -U postgres -d mydb            # connect to a specific database
psql -h localhost -U myuser -d mydb # connect with host, user, database
```

```sql
-- Inside psql: useful meta-commands (start with backslash)
\l              -- list all databases
\c mydb         -- connect (switch) to a database
\dt             -- list all tables in current database
\d tablename    -- describe a table (columns, types, constraints)
\du             -- list all users/roles
\q              -- quit psql
\?              -- help with psql commands
```

> ⚠️ **Common mistake:** Forgetting the semicolon `;` at the end of SQL statements. Unlike Python, SQL requires it — the query simply won't run without it.

---

## Creating databases and users
```sql
-- Connect as postgres superuser first

-- Create a database
CREATE DATABASE shop_db;

-- Create a user with a password
CREATE USER shop_user WITH PASSWORD 'securepass123';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE shop_db TO shop_user;

-- Connect to the new database
\c shop_db

-- Drop a database (careful — permanent!)
DROP DATABASE old_db;
```

---

## Data types in PostgreSQL
```sql
-- Numeric types
INTEGER         -- whole numbers: -2147483648 to 2147483647
BIGINT          -- large whole numbers
NUMERIC(10, 2)  -- exact decimal, e.g. money: 12345678.99
REAL            -- approximate float (avoid for money!)

-- Text types
VARCHAR(100)    -- variable-length text up to 100 characters
TEXT            -- unlimited length text
CHAR(10)        -- fixed-length, padded with spaces

-- Boolean
BOOLEAN         -- TRUE or FALSE (or NULL)

-- Date & time
DATE            -- '2024-03-15'
TIME            -- '14:30:00'
TIMESTAMP       -- '2024-03-15 14:30:00'
TIMESTAMPTZ     -- timestamp with timezone (recommended)

-- Auto-incrementing primary key
SERIAL          -- auto-increment integer (shorthand for INTEGER + SEQUENCE)
BIGSERIAL       -- big auto-increment
```

> ⚠️ **Common mistake:** Using `REAL` or `FLOAT` for money amounts. Floating point numbers cannot represent all decimal values exactly — `0.1 + 0.2` is `0.30000000000000004`. Always use `NUMERIC(precision, scale)` for currency.

---

## Creating tables — DDL (Data Definition Language)
```sql
-- DDL commands define the *structure* of data

-- Create a customers table
CREATE TABLE customers (
    id          SERIAL PRIMARY KEY,           -- auto-increment unique id
    name        VARCHAR(100) NOT NULL,        -- required, max 100 chars
    email       VARCHAR(150) UNIQUE NOT NULL, -- required, must be unique
    phone       VARCHAR(20),                  -- optional
    created_at  TIMESTAMPTZ DEFAULT NOW()     -- auto-set on insert
);

-- Create an orders table with a foreign key
CREATE TABLE orders (
    id           SERIAL PRIMARY KEY,
    customer_id  INTEGER NOT NULL REFERENCES customers(id), -- foreign key
    product      VARCHAR(200) NOT NULL,
    amount       NUMERIC(12, 2) NOT NULL,
    ordered_at   TIMESTAMPTZ DEFAULT NOW()
);

-- Delete a table (permanent — all data lost)
DROP TABLE orders;

-- Delete a table only if it exists (safer)
DROP TABLE IF EXISTS orders;

-- Add a column to an existing table
ALTER TABLE customers ADD COLUMN address TEXT;

-- Rename a column
ALTER TABLE customers RENAME COLUMN phone TO phone_number;
```

> ⚠️ **Common mistake:** Running `DROP TABLE` when you meant to run `DELETE FROM`. `DROP TABLE` deletes the entire table structure AND all its data permanently. `DELETE FROM` only removes rows. Know the difference before you type it.

---

## Inserting and selecting data — DML basics
```sql
-- DML = Data Manipulation Language: INSERT, SELECT, UPDATE, DELETE

-- Insert a row
INSERT INTO customers (name, email, phone)
VALUES ('Nilufar Karimova', 'nilufar@mail.com', '+998901234567');

-- Insert multiple rows at once
INSERT INTO customers (name, email) VALUES
    ('Sardor Toshmatov', 'sardor@mail.com'),
    ('Malika Yusupova',  'malika@mail.com');

-- Insert and return the generated id
INSERT INTO customers (name, email)
VALUES ('Bobur Alimov', 'bobur@mail.com')
RETURNING id, created_at;

-- Select all rows and all columns
SELECT * FROM customers;

-- Select specific columns
SELECT name, email FROM customers;

-- Filter with WHERE
SELECT * FROM customers WHERE name = 'Nilufar Karimova';

-- Select with a condition
SELECT * FROM orders WHERE amount > 100000;
```

---

## Quick reference

| Command / Type | What it does | Example |
|---|---|---|
| `CREATE DATABASE` | Create a new database | `CREATE DATABASE shop_db;` |
| `CREATE TABLE` | Define a new table | `CREATE TABLE products (...);` |
| `DROP TABLE IF EXISTS` | Delete table safely | `DROP TABLE IF EXISTS orders;` |
| `ALTER TABLE ADD COLUMN` | Add column to existing table | `ALTER TABLE t ADD COLUMN x TEXT;` |
| `SERIAL PRIMARY KEY` | Auto-increment unique ID | `id SERIAL PRIMARY KEY` |
| `NOT NULL` | Column is required | `name VARCHAR(100) NOT NULL` |
| `UNIQUE` | No duplicate values allowed | `email VARCHAR(150) UNIQUE` |
| `REFERENCES` | Foreign key constraint | `REFERENCES customers(id)` |
| `DEFAULT NOW()` | Auto-set current timestamp | `created_at TIMESTAMPTZ DEFAULT NOW()` |
| `NUMERIC(12,2)` | Exact decimal for money | `price NUMERIC(12,2)` |
| `INSERT INTO ... VALUES` | Add a row | `INSERT INTO t (col) VALUES (val);` |
| `SELECT * FROM` | Read all rows | `SELECT * FROM customers;` |
| `\dt` | List tables in psql | `\dt` |
| `\d tablename` | Describe table structure | `\d customers` |

---

## Task list
1. PostgreSQL installation & first connection
2. Create the coffee shop database
3. Design the library database
4. Build the hospital schema
5. Insert and inspect real data

---

## SQL LeetCode
- [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/) — 🟢 Easy
- [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) — 🟢 Easy

