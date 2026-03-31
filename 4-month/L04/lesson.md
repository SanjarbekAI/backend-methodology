# L37 — SQL: SELECT, Filtering & Sorting

## Why this matters
The `SELECT` statement is the most-used SQL command in existence. Every report, every API response, every dashboard is powered by `SELECT` queries. Writing fast, precise queries is a core backend skill — the difference between an app that loads in 50ms and one that times out under real traffic.

---

## Topics

## SELECT — Reading data from tables
```sql
-- Basic syntax
SELECT column1, column2 FROM table_name;

-- Select everything (use sparingly in production — pulls unnecessary data)
SELECT * FROM products;

-- Select with an alias — rename a column in the result
SELECT name, price AS unit_price, stock AS units_available
FROM products;

-- Select a computed value
SELECT name, price, price * 0.12 AS tax_amount, price * 1.12 AS total_with_tax
FROM products;

-- Select only unique values
SELECT DISTINCT category FROM products;

-- Count rows
SELECT COUNT(*) FROM products;
SELECT COUNT(*) AS total_products FROM products;
```

> ⚠️ **Common mistake:** Using `SELECT *` in application code. It transfers all columns even ones you don't need, slows down queries, and breaks if someone adds or reorders columns. Always name the columns you actually need.

---

## WHERE — Filtering rows
```sql
-- Equality
SELECT * FROM customers WHERE city = 'Tashkent';

-- Comparison operators
SELECT * FROM orders WHERE amount > 500000;
SELECT * FROM products WHERE stock <= 10;
SELECT * FROM orders WHERE amount != 0;

-- Multiple conditions
SELECT * FROM products WHERE category = 'Electronics' AND price < 1000000;
SELECT * FROM products WHERE stock = 0 OR stock IS NULL;

-- NOT
SELECT * FROM customers WHERE NOT city = 'Samarkand';

-- Range with BETWEEN (inclusive on both ends)
SELECT * FROM orders WHERE amount BETWEEN 100000 AND 500000;
SELECT * FROM products WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';

-- List of values with IN
SELECT * FROM customers WHERE city IN ('Tashkent', 'Samarkand', 'Bukhara');
SELECT * FROM orders WHERE status IN ('pending', 'processing');

-- NOT IN
SELECT * FROM products WHERE category NOT IN ('Archived', 'Draft');
```

> ⚠️ **Common mistake:** Using `= NULL` to check for null values. This **never works** in SQL — `NULL = NULL` is `NULL`, not `TRUE`. Always use `IS NULL` or `IS NOT NULL`.

```sql
-- WRONG
SELECT * FROM customers WHERE phone = NULL;   -- returns nothing!

-- CORRECT
SELECT * FROM customers WHERE phone IS NULL;
SELECT * FROM customers WHERE phone IS NOT NULL;
```

---

## LIKE — Pattern matching in text
```sql
-- % matches any sequence of characters
-- _ matches exactly one character

SELECT * FROM customers WHERE name LIKE 'A%';         -- starts with A
SELECT * FROM customers WHERE name LIKE '%ov';        -- ends with ov
SELECT * FROM customers WHERE email LIKE '%@gmail%';  -- contains @gmail
SELECT * FROM products WHERE name LIKE '_aps%';       -- second char is 'a'

-- Case-insensitive search (PostgreSQL specific)
SELECT * FROM customers WHERE name ILIKE 'nilufar%';  -- ILIKE ignores case
```

---

## ORDER BY — Sorting results
```sql
-- Sort ascending (default)
SELECT * FROM products ORDER BY price;
SELECT * FROM products ORDER BY price ASC;

-- Sort descending
SELECT * FROM products ORDER BY price DESC;

-- Sort by multiple columns
SELECT * FROM orders ORDER BY customer_id ASC, ordered_at DESC;

-- Sort by alias
SELECT name, price * 1.12 AS total FROM products ORDER BY total DESC;

-- NULLs sort last by default in ASC, first in DESC
-- Override this:
SELECT * FROM products ORDER BY price ASC NULLS LAST;
```

---

## LIMIT & OFFSET — Pagination
```sql
-- Get only the first 10 rows
SELECT * FROM products ORDER BY price DESC LIMIT 10;

-- Get rows 11-20 (page 2, page size 10)
SELECT * FROM products ORDER BY price DESC LIMIT 10 OFFSET 10;

-- Get the single most expensive product
SELECT * FROM products ORDER BY price DESC LIMIT 1;

-- Get the 3 most recent orders
SELECT * FROM orders ORDER BY ordered_at DESC LIMIT 3;
```

> ⚠️ **Common mistake:** Using `LIMIT` without `ORDER BY`. Without ordering, the database returns rows in an undefined order — you might get different rows each time. Always `ORDER BY` before paginating.

---

## CASE WHEN — Conditional logic in queries
```sql
-- Add a computed "label" column based on a condition
SELECT
    name,
    price,
    CASE
        WHEN price < 50000   THEN 'Budget'
        WHEN price < 200000  THEN 'Mid-range'
        WHEN price < 1000000 THEN 'Premium'
        ELSE 'Luxury'
    END AS price_tier
FROM products
ORDER BY price;

-- Use CASE to flag low stock
SELECT
    name,
    stock,
    CASE WHEN stock = 0 THEN 'OUT OF STOCK'
         WHEN stock < 5 THEN 'LOW STOCK'
         ELSE 'In Stock'
    END AS stock_status
FROM products;
```

---

## String & numeric functions
```sql
-- String functions
SELECT UPPER(name) FROM customers;           -- 'nilufar' → 'NILUFAR'
SELECT LOWER(email) FROM customers;          -- normalize to lowercase
SELECT LENGTH(name) FROM customers;          -- character count
SELECT TRIM(name) FROM customers;            -- remove leading/trailing spaces
SELECT CONCAT(first_name, ' ', last_name);   -- combine columns
SELECT name || ' (' || category || ')';      -- string concatenation with ||
SELECT SUBSTRING(name, 1, 3) FROM products;  -- first 3 chars

-- Numeric functions
SELECT ROUND(price * 1.12, 2) AS total;      -- round to 2 decimal places
SELECT CEIL(price / 100.0) AS price_hundreds;
SELECT ABS(balance) FROM accounts;           -- absolute value

-- Null handling
SELECT COALESCE(phone, 'No phone') FROM customers;  -- return default if NULL
```

---

## Quick reference

| Clause / Function | What it does | Example |
|---|---|---|
| `SELECT col AS alias` | Rename column in result | `SELECT price AS cost` |
| `DISTINCT` | Remove duplicate rows | `SELECT DISTINCT city FROM ...` |
| `WHERE col = val` | Filter rows by equality | `WHERE status = 'active'` |
| `WHERE col IS NULL` | Check for null | `WHERE phone IS NULL` |
| `BETWEEN a AND b` | Inclusive range filter | `WHERE price BETWEEN 1 AND 100` |
| `IN (a, b, c)` | Match any value in list | `WHERE city IN ('A','B')` |
| `LIKE '%pattern%'` | Text pattern match | `WHERE name LIKE 'A%'` |
| `ILIKE` | Case-insensitive LIKE | `WHERE name ILIKE 'ali%'` |
| `ORDER BY col DESC` | Sort descending | `ORDER BY price DESC` |
| `LIMIT n OFFSET m` | Pagination | `LIMIT 10 OFFSET 20` |
| `CASE WHEN...THEN...END` | Conditional label | `CASE WHEN x>0 THEN 'pos'` |
| `COALESCE(col, default)` | Replace NULL with default | `COALESCE(phone, 'N/A')` |
| `ROUND(val, 2)` | Round to decimals | `ROUND(price * 1.12, 2)` |

---

## Task list
1. Product catalog queries — the online store
2. Order search & filtering — the operations dashboard
3. Customer directory — sorted and paginated
4. Inventory status report — CASE WHEN
5. String & null cleanup — the data quality audit

---

## SQL LeetCode
- [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) — 🟢 Easy
- [Rising Temperature](https://leetcode.com/problems/rising-temperature/) — 🟢 Easy

