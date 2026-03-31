# L40 — SQL: DDL, Constraints & Indexes

## Why this matters
A database without constraints is a liability — bad data gets in, silent errors corrupt your reports, and debugging becomes a nightmare. Indexes are what separate a query that runs in 2ms from one that takes 45 seconds on a large table. This lesson is about designing databases that are both safe and fast — professional-grade database engineering.

---

## Topics

## UPDATE & DELETE — Modifying and removing data

```sql
-- UPDATE: change existing rows
UPDATE products
SET price = 450000
WHERE id = 3;

-- Update multiple columns at once
UPDATE customers
SET city = 'Tashkent', phone = '+998901234567'
WHERE id = 5;

-- Update with a computed value
UPDATE products
SET price = price * 1.10          -- increase all prices by 10%
WHERE category = 'Electronics';

-- Update based on a subquery
UPDATE orders
SET status = 'cancelled'
WHERE customer_id IN (
    SELECT id FROM customers WHERE is_blocked = TRUE
);

-- RETURNING: see what was changed
UPDATE products
SET stock = stock - 1
WHERE id = 7
RETURNING id, name, stock;

-- DELETE: remove rows
DELETE FROM orders WHERE status = 'cancelled' AND ordered_at < NOW() - INTERVAL '1 year';

-- Delete all rows but keep the table structure
DELETE FROM temp_logs;

-- Faster for full table wipe (no row-by-row log, no RETURNING)
TRUNCATE TABLE temp_logs;

-- Delete and see what was removed
DELETE FROM orders WHERE id = 12 RETURNING *;
```

> ⚠️ **Common mistake:** Running `UPDATE` or `DELETE` without a `WHERE` clause. `UPDATE products SET price = 0` sets ALL product prices to 0. Always write the `WHERE` first, test it with a `SELECT`, then switch to `UPDATE`/`DELETE`.

---

## Constraints — Enforcing data integrity
Constraints are rules the database enforces automatically — regardless of what Python code tries to insert.

```sql
-- PRIMARY KEY: unique, not null, one per table
CREATE TABLE users (
    id SERIAL PRIMARY KEY
);

-- NOT NULL: column is required
ALTER TABLE users ADD COLUMN email VARCHAR(150) NOT NULL;

-- UNIQUE: no two rows can have the same value
ALTER TABLE users ADD CONSTRAINT users_email_unique UNIQUE (email);

-- CHECK: custom validation rule
ALTER TABLE products ADD CONSTRAINT price_positive CHECK (price > 0);
ALTER TABLE employees ADD CONSTRAINT valid_salary CHECK (salary BETWEEN 500000 AND 100000000);
ALTER TABLE orders ADD CONSTRAINT valid_status
    CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled'));

-- FOREIGN KEY with CASCADE behavior
CREATE TABLE orders (
    id          SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL
        REFERENCES customers(id)
        ON DELETE CASCADE     -- delete orders when customer is deleted
        ON UPDATE CASCADE     -- update order.customer_id if customers.id changes
);

-- Other CASCADE options:
-- ON DELETE SET NULL    → set customer_id to NULL when customer deleted
-- ON DELETE RESTRICT    → prevent customer deletion if they have orders (default)
-- ON DELETE NO ACTION   → same as RESTRICT but deferred

-- DEFAULT values
ALTER TABLE orders ADD COLUMN created_at TIMESTAMPTZ DEFAULT NOW();
ALTER TABLE products ADD COLUMN is_active BOOLEAN DEFAULT TRUE;
```

> ⚠️ **Common mistake:** Using `ON DELETE CASCADE` without thinking about it. If you cascade-delete a customer, ALL their orders, order_items, invoices, and anything else referencing them will also be deleted silently. Use `ON DELETE RESTRICT` (the default) when data should never be deleted without explicit cleanup.

---

## Named constraints & altering constraints

```sql
-- Add a named constraint (recommended — easier to drop later)
ALTER TABLE products
ADD CONSTRAINT products_price_positive CHECK (price > 0);

-- Drop a constraint by name
ALTER TABLE products
DROP CONSTRAINT products_price_positive;

-- Add a UNIQUE constraint on multiple columns together
ALTER TABLE order_items
ADD CONSTRAINT order_items_unique_per_order UNIQUE (order_id, product_id);

-- View all constraints on a table
SELECT conname, contype, consrc
FROM pg_constraint
WHERE conrelid = 'products'::regclass;

-- In psql:
\d products    -- shows all columns, constraints, and indexes
```

---

## Indexes — Making queries fast
An **index** is a separate data structure that lets PostgreSQL find rows without scanning every row in the table. Without an index on a WHERE condition, PostgreSQL reads every single row — called a **sequential scan (Seq Scan)**. With an index, it jumps directly to matching rows — called an **index scan**.

```sql
-- Create a basic B-tree index (default type — good for =, <, >, BETWEEN, ORDER BY)
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_products_category ON products(category);

-- Unique index (also enforces uniqueness — same as UNIQUE constraint)
CREATE UNIQUE INDEX idx_customers_email ON customers(email);

-- Composite index (multiple columns — order matters!)
-- Best for: WHERE category = 'X' AND price < 100
-- Not useful for: WHERE price < 100 (without category)
CREATE INDEX idx_products_category_price ON products(category, price);

-- Partial index (index only a subset of rows — smaller, faster)
-- Useful when queries always filter on a condition
CREATE INDEX idx_active_products ON products(name) WHERE is_active = TRUE;
CREATE INDEX idx_pending_orders ON orders(customer_id) WHERE status = 'pending';

-- Index on expression
CREATE INDEX idx_customers_lower_email ON customers(LOWER(email));
-- Now this query uses the index:
-- SELECT * FROM customers WHERE LOWER(email) = 'user@mail.com';

-- Drop an index
DROP INDEX idx_products_category;

-- List all indexes in the current database
SELECT indexname, tablename, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename;
```

---

## EXPLAIN ANALYZE — Understanding query performance

```sql
-- EXPLAIN: show the query plan (no execution)
EXPLAIN SELECT * FROM orders WHERE customer_id = 5;

-- EXPLAIN ANALYZE: execute AND show actual timing
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 5;

-- Output shows:
-- Seq Scan      → reading every row (slow on large tables)
-- Index Scan    → using an index (fast)
-- Bitmap Scan   → hybrid approach for medium selectivity
-- cost=0.00..X  → estimated cost (arbitrary units, lower is better)
-- actual time=  → real execution time in ms
-- rows=         → actual rows returned

-- Test the difference: run before and after creating an index
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 5;
CREATE INDEX idx_orders_customer ON orders(customer_id);
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 5;
-- You will see the plan change from Seq Scan to Index Scan
```

> ⚠️ **Common mistake:** Over-indexing. Every index makes `INSERT`, `UPDATE`, and `DELETE` slower because PostgreSQL must update all indexes too. Only index columns that appear frequently in `WHERE`, `JOIN ON`, or `ORDER BY` clauses. Never index every column "just in case."

---

## Database migrations concept

```sql
-- In real projects, schema changes are tracked as numbered migration files
-- migration_001_create_users.sql
-- migration_002_add_phone_to_users.sql
-- migration_003_create_orders.sql

-- Always write migrations to be reversible:

-- UP migration (apply the change)
ALTER TABLE customers ADD COLUMN loyalty_points INTEGER DEFAULT 0;

-- DOWN migration (undo the change — always write this too)
ALTER TABLE customers DROP COLUMN loyalty_points;
```

---

## Quick reference

| Command | What it does | Example |
|---|---|---|
| `UPDATE ... SET ... WHERE` | Modify matching rows | `UPDATE p SET price=100 WHERE id=1` |
| `DELETE FROM ... WHERE` | Remove matching rows | `DELETE FROM orders WHERE id=5` |
| `TRUNCATE TABLE` | Delete all rows fast | `TRUNCATE TABLE logs` |
| `RETURNING` | Show changed rows | `DELETE FROM x WHERE ... RETURNING *` |
| `NOT NULL` | Column is required | `email VARCHAR NOT NULL` |
| `UNIQUE` | No duplicates allowed | `UNIQUE (email)` |
| `CHECK (...)` | Custom validation rule | `CHECK (price > 0)` |
| `ON DELETE CASCADE` | Auto-delete child rows | `REFERENCES t(id) ON DELETE CASCADE` |
| `ON DELETE RESTRICT` | Prevent parent deletion | `REFERENCES t(id) ON DELETE RESTRICT` |
| `CREATE INDEX` | Speed up queries | `CREATE INDEX idx ON t(col)` |
| `CREATE INDEX ... WHERE` | Partial index | `CREATE INDEX i ON t(col) WHERE active` |
| `EXPLAIN ANALYZE` | Show query plan + timing | `EXPLAIN ANALYZE SELECT ...` |
| `DROP CONSTRAINT` | Remove a constraint | `ALTER TABLE t DROP CONSTRAINT name` |

---

## Task list
1. Safe updates — the price adjustment tool
2. Constraint fortress — a bulletproof orders table
3. Cascade decisions — designing safe foreign keys
4. Index workshop — before and after performance
5. Migration script — version-controlled schema changes

---

## SQL LeetCode
- [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) — 🟢 Easy
- [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) — 🟠 Medium

