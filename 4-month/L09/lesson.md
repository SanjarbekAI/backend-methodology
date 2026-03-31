# L42 — Advanced Queries & Transactions

## Why this matters
Transactions are the safety net of every serious database application — they guarantee that a sequence of operations either all succeed or all fail together. Window functions unlock analytics queries that would otherwise require dozens of lines of Python. Views and stored procedures let you hide complexity and share query logic across your entire application. This lesson makes you dangerous with PostgreSQL.

---

## Topics

## Transactions — Atomicity & safety
A **transaction** is a group of SQL statements that are treated as a single unit. Either ALL statements succeed (commit) or ALL are undone (rollback). This is the ACID guarantee.

```sql
-- Explicit transaction block
BEGIN;                                      -- start a transaction

UPDATE accounts SET balance = balance - 500000 WHERE id = 1;   -- debit sender
UPDATE accounts SET balance = balance + 500000 WHERE id = 2;   -- credit receiver

-- If both succeed:
COMMIT;                                     -- make both changes permanent

-- If anything goes wrong:
ROLLBACK;                                   -- undo everything since BEGIN
```

```sql
-- SAVEPOINT: partial rollback within a transaction
BEGIN;

INSERT INTO orders (customer_id, amount) VALUES (1, 850000);
SAVEPOINT after_order;

INSERT INTO order_items (order_id, product_id, quantity) VALUES (99, 5, 2);
-- This fails because order_id=99 doesn't exist

ROLLBACK TO SAVEPOINT after_order;   -- undo only the failed INSERT, keep the order
-- Now fix the issue and continue...
INSERT INTO order_items (order_id, product_id, quantity) VALUES (currval('orders_id_seq'), 5, 2);

COMMIT;
```

> ⚠️ **Common mistake:** Not wrapping multi-step operations in a transaction. A bank transfer that debits one account but fails before crediting the other (due to a crash or error) will permanently lose money. Transactions prevent this.

---

## Window functions — Analytics without GROUP BY collapsing
Window functions compute values **across a set of rows** without collapsing them into one row (unlike `GROUP BY`). They are the most powerful tool for rankings, running totals, and comparisons.

```sql
-- Syntax: function() OVER (PARTITION BY ... ORDER BY ...)

-- RANK: rank employees by salary within their department
SELECT
    name,
    department,
    salary,
    RANK()       OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_dense_rank,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num
FROM employees;

-- Difference between RANK, DENSE_RANK, ROW_NUMBER:
-- Salaries: 10, 10, 8
-- RANK:        1,  1, 3   (skips 2)
-- DENSE_RANK:  1,  1, 2   (no skip)
-- ROW_NUMBER:  1,  2, 3   (always unique)

-- LAG and LEAD: compare each row to the previous/next row
SELECT
    month,
    revenue,
    LAG(revenue)  OVER (ORDER BY month) AS prev_month_revenue,
    revenue - LAG(revenue) OVER (ORDER BY month) AS month_over_month_change
FROM monthly_sales;

-- Running total (cumulative SUM)
SELECT
    ordered_at::date AS sale_date,
    amount,
    SUM(amount) OVER (ORDER BY ordered_at) AS cumulative_revenue
FROM orders
WHERE status = 'completed'
ORDER BY ordered_at;

-- Moving average (last 3 rows)
SELECT
    sale_date,
    revenue,
    AVG(revenue) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_3
FROM daily_revenue;

-- FIRST_VALUE and LAST_VALUE
SELECT
    name, department, salary,
    FIRST_VALUE(name) OVER (PARTITION BY department ORDER BY salary DESC) AS top_earner
FROM employees;
```

> ⚠️ **Common mistake:** Using `WHERE` to filter on a window function result — this doesn't work. Window functions are evaluated after `WHERE`. To filter on a window function result, wrap it in a CTE or subquery.

```sql
-- WRONG
SELECT name, salary, RANK() OVER (ORDER BY salary DESC) AS rnk
FROM employees
WHERE rnk <= 3;   -- ERROR: column "rnk" does not exist in WHERE

-- CORRECT: use a CTE
WITH ranked AS (
    SELECT name, salary, RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT * FROM ranked WHERE rnk <= 3;
```

---

## Views — Saved queries as virtual tables
A **view** is a named, saved SQL query. It looks like a table but doesn't store data — every time you query it, the underlying query runs.

```sql
-- Create a view
CREATE VIEW active_products AS
SELECT id, name, category, price, stock
FROM products
WHERE is_active = TRUE
ORDER BY name;

-- Use it like a table
SELECT * FROM active_products WHERE category = 'Electronics';

-- Update a view
CREATE OR REPLACE VIEW active_products AS
SELECT id, name, category, price, stock, created_at
FROM products
WHERE is_active = TRUE;

-- Drop a view
DROP VIEW IF EXISTS active_products;

-- Complex view: orders with customer and product details
CREATE VIEW order_details AS
SELECT
    o.id         AS order_id,
    c.full_name  AS customer,
    c.email,
    p.name       AS product,
    oi.quantity,
    oi.quantity * p.price AS line_total,
    o.status,
    o.ordered_at
FROM orders AS o
JOIN customers AS c    ON o.customer_id = c.id
JOIN order_items AS oi ON oi.order_id   = o.id
JOIN products AS p     ON oi.product_id = p.id;

-- Now from Python, you can query this view like any table:
-- SELECT * FROM order_details WHERE status = 'completed'
```

---

## Stored procedures & functions (PL/pgSQL basics)

```sql
-- A function that returns a value
CREATE OR REPLACE FUNCTION get_customer_total(p_customer_id INTEGER)
RETURNS NUMERIC AS $$
BEGIN
    RETURN (
        SELECT COALESCE(SUM(amount), 0)
        FROM orders
        WHERE customer_id = p_customer_id AND status = 'completed'
    );
END;
$$ LANGUAGE plpgsql;

-- Call the function
SELECT get_customer_total(5);
SELECT full_name, get_customer_total(id) AS total_spent FROM customers;

-- A procedure that performs an action (no return value)
CREATE OR REPLACE PROCEDURE process_order(p_order_id INTEGER)
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE orders SET status = 'processing' WHERE id = p_order_id;
    INSERT INTO order_log (order_id, event, logged_at)
    VALUES (p_order_id, 'moved to processing', NOW());
    COMMIT;
END;
$$;

-- Call a procedure
CALL process_order(42);
```

---

## Transactions in Python (psycopg2)

```python
import psycopg2
from psycopg2 import errors as pg_errors

def transfer_funds(conn, from_id: int, to_id: int, amount: float) -> bool:
    """Transfer funds between accounts atomically."""
    try:
        with conn.cursor() as cur:
            # Check sender has enough balance
            cur.execute("SELECT balance FROM accounts WHERE id = %s FOR UPDATE", (from_id,))
            row = cur.fetchone()
            if not row or row[0] < amount:
                conn.rollback()
                return False

            # Debit sender
            cur.execute(
                "UPDATE accounts SET balance = balance - %s WHERE id = %s",
                (amount, from_id)
            )
            # Credit receiver
            cur.execute(
                "UPDATE accounts SET balance = balance + %s WHERE id = %s",
                (amount, to_id)
            )
            # Log the transfer
            cur.execute(
                "INSERT INTO transfer_log (from_id, to_id, amount) VALUES (%s, %s, %s)",
                (from_id, to_id, amount)
            )
        conn.commit()           # all three operations succeed together
        return True

    except pg_errors.ForeignKeyViolation:
        conn.rollback()         # undo everything if any step fails
        return False
    except psycopg2.DatabaseError:
        conn.rollback()
        raise
```

---

## Quick reference

| Feature | Syntax | Notes |
|---|---|---|
| `BEGIN` / `COMMIT` / `ROLLBACK` | `BEGIN; ...; COMMIT;` | Atomic group of statements |
| `SAVEPOINT` | `SAVEPOINT name;` | Partial rollback point |
| `RANK()` | `RANK() OVER (ORDER BY col DESC)` | Gaps on ties |
| `DENSE_RANK()` | `DENSE_RANK() OVER (...)` | No gaps on ties |
| `ROW_NUMBER()` | `ROW_NUMBER() OVER (...)` | Always unique |
| `LAG(col)` | `LAG(col) OVER (ORDER BY ...)` | Previous row's value |
| `LEAD(col)` | `LEAD(col) OVER (ORDER BY ...)` | Next row's value |
| Running total | `SUM(col) OVER (ORDER BY ...)` | Cumulative sum |
| `PARTITION BY` | `OVER (PARTITION BY dept ORDER BY sal)` | Window per group |
| `CREATE VIEW` | `CREATE VIEW name AS SELECT ...` | Saved query |
| `FOR UPDATE` | `SELECT ... FOR UPDATE` | Lock rows in a transaction |

---

## Task list
1. The bank transfer — transactions in action
2. Sales leaderboard — window functions
3. Monthly trend analyzer — LAG and running totals
4. The order dashboard view — creating useful views
5. Full transaction app — Python + multi-step transactions

---

## SQL LeetCode
- [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) — 🔴 Hard
- [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) — 🟠 Medium

