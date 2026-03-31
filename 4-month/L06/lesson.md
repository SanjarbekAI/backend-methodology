# L39 — SQL: Aggregations, GROUP BY & Subqueries

## Why this matters
Raw rows are rarely what a business needs. A manager doesn't want to see 50,000 order rows — she wants to see total revenue per month, best-selling products, average order value per city. Aggregations and GROUP BY are how you turn raw data into business intelligence. Subqueries let you build multi-step logic inside a single SQL statement — the equivalent of nested function calls in Python.

---

## Topics

## Aggregate functions — Computing summaries
Aggregate functions collapse many rows into a single computed value.

```sql
-- COUNT: how many rows?
SELECT COUNT(*) FROM orders;                        -- total rows including NULLs
SELECT COUNT(phone) FROM customers;                 -- only non-NULL phone values
SELECT COUNT(DISTINCT city) FROM customers;         -- unique cities

-- SUM: total of a numeric column
SELECT SUM(amount) FROM orders;
SELECT SUM(amount) FROM orders WHERE status = 'completed';

-- AVG: average value
SELECT AVG(amount) FROM orders;
SELECT ROUND(AVG(amount), 2) AS avg_order_value FROM orders;

-- MIN and MAX
SELECT MIN(price) AS cheapest, MAX(price) AS most_expensive FROM products;
SELECT MIN(ordered_at) AS first_order, MAX(ordered_at) AS last_order FROM orders;

-- Combine multiple aggregates in one query
SELECT
    COUNT(*)               AS total_orders,
    SUM(amount)            AS total_revenue,
    ROUND(AVG(amount), 2)  AS avg_order,
    MIN(amount)            AS smallest_order,
    MAX(amount)            AS largest_order
FROM orders
WHERE status = 'completed';
```

> ⚠️ **Common mistake:** Using `COUNT(column_name)` when you want to count all rows — if the column has NULLs, they are excluded from the count. Use `COUNT(*)` to count all rows regardless of NULL values.

---

## GROUP BY — Aggregating per category
`GROUP BY` splits rows into groups and applies the aggregate function to each group separately.

```sql
-- Total revenue per city
SELECT city, SUM(amount) AS total_revenue
FROM orders
INNER JOIN customers ON orders.customer_id = customers.id
GROUP BY city
ORDER BY total_revenue DESC;

-- Count of orders per status
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status;

-- Average order value per customer
SELECT
    c.full_name,
    COUNT(o.id)           AS num_orders,
    SUM(o.amount)         AS total_spent,
    ROUND(AVG(o.amount), 2) AS avg_order
FROM orders AS o
INNER JOIN customers AS c ON o.customer_id = c.id
GROUP BY c.id, c.full_name
ORDER BY total_spent DESC;

-- Group by multiple columns
SELECT category, brand, COUNT(*) AS product_count, AVG(price) AS avg_price
FROM products
GROUP BY category, brand
ORDER BY category, avg_price DESC;
```

> ⚠️ **Common mistake:** Putting a non-aggregated column in `SELECT` that is NOT in `GROUP BY`. PostgreSQL will give you an error: *"column must appear in GROUP BY clause or be used in aggregate function."* Every column in `SELECT` must either be in `GROUP BY` or wrapped in an aggregate function.

---

## HAVING — Filtering groups
`WHERE` filters individual rows **before** grouping. `HAVING` filters groups **after** grouping.

```sql
-- WHERE: filters rows before grouping
-- HAVING: filters the result of GROUP BY

-- Customers who have spent more than 1,000,000 sum total
SELECT
    c.full_name,
    SUM(o.amount) AS total_spent
FROM orders AS o
INNER JOIN customers AS c ON o.customer_id = c.id
GROUP BY c.id, c.full_name
HAVING SUM(o.amount) > 1000000
ORDER BY total_spent DESC;

-- Categories with more than 5 products
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category
HAVING COUNT(*) > 5;

-- Cities where average order value is above 500,000
SELECT c.city, ROUND(AVG(o.amount), 2) AS avg_order
FROM orders AS o
INNER JOIN customers AS c ON o.customer_id = c.id
GROUP BY c.city
HAVING AVG(o.amount) > 500000
ORDER BY avg_order DESC;
```

---

## The full SQL query order of execution
Understanding this order prevents most GROUP BY mistakes:

```
1. FROM          → which tables?
2. JOIN          → combine tables
3. WHERE         → filter rows (before grouping)
4. GROUP BY      → split into groups
5. HAVING        → filter groups
6. SELECT        → choose columns / compute aggregates
7. DISTINCT      → remove duplicates
8. ORDER BY      → sort
9. LIMIT/OFFSET  → paginate
```

---

## Subqueries — Queries inside queries
A **subquery** is a SELECT statement nested inside another SQL statement. Use it when you need to use the result of one query as input to another.

```sql
-- Scalar subquery: returns a single value
-- Find all products priced above the average price
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)
ORDER BY price DESC;

-- Find the most expensive product in each category
SELECT name, category, price
FROM products
WHERE price = (
    SELECT MAX(price) FROM products AS p2
    WHERE p2.category = products.category
);

-- Subquery in FROM clause (derived table / inline view)
SELECT city, avg_spent
FROM (
    SELECT c.city, AVG(o.amount) AS avg_spent
    FROM orders AS o
    INNER JOIN customers AS c ON o.customer_id = c.id
    GROUP BY c.city
) AS city_stats
WHERE avg_spent > 300000
ORDER BY avg_spent DESC;

-- EXISTS: check if matching rows exist (often faster than IN for large datasets)
SELECT c.full_name
FROM customers AS c
WHERE EXISTS (
    SELECT 1 FROM orders AS o
    WHERE o.customer_id = c.id AND o.status = 'completed'
);

-- NOT EXISTS: find customers with NO completed orders
SELECT c.full_name
FROM customers AS c
WHERE NOT EXISTS (
    SELECT 1 FROM orders AS o
    WHERE o.customer_id = c.id AND o.status = 'completed'
);
```

---

## CTEs — Common Table Expressions (WITH clause)
CTEs are named subqueries that make complex queries readable. Think of them as temporary named results — like variables in SQL.

```sql
-- WITHOUT CTE: hard to read
SELECT full_name, total_spent
FROM (
    SELECT c.full_name, SUM(o.amount) AS total_spent
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    GROUP BY c.id, c.full_name
) AS spending
WHERE total_spent > 1000000;

-- WITH CTE: clean and readable
WITH customer_spending AS (
    SELECT
        c.id,
        c.full_name,
        SUM(o.amount) AS total_spent
    FROM customers AS c
    INNER JOIN orders AS o ON c.id = o.customer_id
    GROUP BY c.id, c.full_name
)
SELECT full_name, total_spent
FROM customer_spending
WHERE total_spent > 1000000
ORDER BY total_spent DESC;

-- Multiple CTEs chained
WITH
monthly_revenue AS (
    SELECT DATE_TRUNC('month', ordered_at) AS month, SUM(amount) AS revenue
    FROM orders
    WHERE status = 'completed'
    GROUP BY month
),
avg_monthly AS (
    SELECT AVG(revenue) AS avg_rev FROM monthly_revenue
)
SELECT month, revenue, ROUND(revenue / avg_rev * 100, 1) AS pct_of_avg
FROM monthly_revenue, avg_monthly
ORDER BY month;
```

> ⚠️ **Common mistake:** Writing a deeply nested subquery instead of a CTE when the logic has more than 2 levels. Nested subqueries become unreadable and unmaintainable. As soon as a subquery is referenced twice or the nesting goes beyond 2 levels, use a CTE.

---

## Quick reference

| Function / Clause | What it does | Example |
|---|---|---|
| `COUNT(*)` | Count all rows | `SELECT COUNT(*) FROM orders` |
| `COUNT(col)` | Count non-NULL values | `SELECT COUNT(phone) FROM customers` |
| `SUM(col)` | Total of a column | `SELECT SUM(amount) FROM orders` |
| `AVG(col)` | Average of a column | `SELECT AVG(price) FROM products` |
| `MIN(col)` / `MAX(col)` | Smallest / largest value | `SELECT MIN(price), MAX(price)` |
| `GROUP BY col` | Group rows, aggregate per group | `GROUP BY category` |
| `HAVING condition` | Filter groups after aggregation | `HAVING COUNT(*) > 5` |
| `WHERE` vs `HAVING` | WHERE filters rows; HAVING filters groups | — |
| Subquery in `WHERE` | Filter using result of another query | `WHERE price > (SELECT AVG...)` |
| Subquery in `FROM` | Use a query result as a table | `FROM (SELECT ...) AS alias` |
| `WITH name AS (...)` | Named CTE for readable logic | `WITH stats AS (SELECT ...)` |
| `EXISTS (subquery)` | True if subquery returns any row | `WHERE EXISTS (SELECT 1 FROM ...)` |

---

## Task list
1. Revenue dashboard — aggregations across a store
2. Top performers — GROUP BY with HAVING
3. Monthly trend report — GROUP BY with dates
4. Smart filtering — subqueries in WHERE
5. Executive summary — CTEs with multi-step logic

---

## SQL LeetCode
- [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/) — 🟢 Easy
- [Average Selling Price](https://leetcode.com/problems/average-selling-price/) — 🟢 Easy

