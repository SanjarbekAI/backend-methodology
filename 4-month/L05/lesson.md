# L38 — SQL: JOINs & Relationships

## Why this matters
The entire power of a relational database is the ability to connect tables. Without JOINs, you'd need to run 5 separate queries and combine the results in Python — slow, error-prone, and complex. JOINs let the database do the heavy lifting and return exactly the combined data you need in one query. This is the most important SQL skill for a backend developer.

---

## Topics

## Understanding JOINs — Why they exist
When data is spread across multiple tables (normalized design), JOINs are how you bring it back together for a query.

```
Table: customers          Table: orders
┌────┬──────────┐         ┌────┬─────────────┬────────┐
│ id │ name     │         │ id │ customer_id │ amount │
├────┼──────────┤         ├────┼─────────────┼────────┤
│  1 │ Nilufar  │         │  1 │           1 │ 850000 │
│  2 │ Sardor   │         │  2 │           1 │  45000 │
│  3 │ Malika   │         │  3 │           2 │  95000 │
└────┴──────────┘         └────┴─────────────┴────────┘

-- Without JOIN: you'd need 2 queries and Python logic
-- With JOIN: one query returns customers AND their orders together
```

---

## INNER JOIN — Only matching rows
Returns rows where the join condition is TRUE in **both** tables. Rows with no match are excluded from both sides.

```sql
-- Show each order WITH the customer's name
SELECT
    customers.name,
    orders.id        AS order_id,
    orders.amount
FROM orders
INNER JOIN customers ON orders.customer_id = customers.id;

-- Cleaner with table aliases
SELECT
    c.name,
    o.id        AS order_id,
    o.amount,
    o.status
FROM orders AS o
INNER JOIN customers AS c ON o.customer_id = c.id;

-- INNER JOIN with a WHERE filter
SELECT c.name, o.amount
FROM orders AS o
INNER JOIN customers AS c ON o.customer_id = c.id
WHERE o.amount > 100000
ORDER BY o.amount DESC;
```

> ⚠️ **Common mistake:** Forgetting the `ON` clause. Without it, SQL performs a **Cartesian product** — every row joined with every other row. For 1000 customers × 10000 orders = 10,000,000 rows returned. Your query will hang or crash.

---

## LEFT JOIN — All rows from the left table
Returns **all rows from the left table**, plus matching rows from the right table. If no match, the right-side columns are `NULL`.

```sql
-- Show ALL customers, with their orders (or NULL if they have none)
SELECT
    c.name,
    c.email,
    o.id     AS order_id,
    o.amount AS order_amount
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id
ORDER BY c.name;

-- Find customers who have NEVER placed an order
-- (the magic of LEFT JOIN + IS NULL filter)
SELECT c.name, c.email
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id
WHERE o.id IS NULL;
```

> 💡 **Analogy:** `INNER JOIN` is like finding only the couples where both people showed up to a party. `LEFT JOIN` is listing every person from the guest list — whether or not their partner showed up. The ones who came alone have `NULL` for their partner's name.

---

## RIGHT JOIN & FULL OUTER JOIN
```sql
-- RIGHT JOIN: all rows from right table, matching from left (rarely used)
-- Usually rewritten as LEFT JOIN by swapping table order
SELECT c.name, o.id AS order_id
FROM orders AS o
RIGHT JOIN customers AS c ON o.customer_id = c.id;
-- This is identical to:
SELECT c.name, o.id AS order_id
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id;

-- FULL OUTER JOIN: all rows from BOTH tables, NULLs where no match
SELECT c.name, o.id AS order_id
FROM customers AS c
FULL OUTER JOIN orders AS o ON c.id = o.customer_id;
```

---

## Joining multiple tables
Real queries often join 3, 4, or more tables. Each `JOIN` adds one more connection.

```sql
-- 3-table join: order details with customer name AND product info
SELECT
    c.name          AS customer,
    p.name          AS product,
    p.category,
    oi.quantity,
    oi.quantity * p.price AS line_total
FROM order_items AS oi
INNER JOIN orders    AS o  ON oi.order_id   = o.id
INNER JOIN customers AS c  ON o.customer_id = c.id
INNER JOIN products  AS p  ON oi.product_id = p.id
WHERE o.status = 'completed'
ORDER BY line_total DESC;
```

---

## Self JOIN — A table joined to itself
Used when a table has a relationship with itself (e.g., an employee has a `manager_id` that points to another employee).

```sql
-- Find each employee and their manager's name
SELECT
    e.name    AS employee,
    m.name    AS manager
FROM employees AS e
LEFT JOIN employees AS m ON e.manager_id = m.id
ORDER BY m.name NULLS LAST;

-- Find employees who earn more than their manager
SELECT e.name AS employee, e.salary, m.name AS manager, m.salary AS mgr_salary
FROM employees AS e
INNER JOIN employees AS m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

---

## USING & NATURAL JOIN (shortcuts)
```sql
-- USING: when both tables have the same column name for the join key
SELECT c.name, o.amount
FROM customers AS c
INNER JOIN orders AS o USING (id);   -- only when column is literally named 'id' in both

-- NATURAL JOIN: auto-joins on ALL identically named columns (avoid in production)
-- Dangerous because schema changes silently change query behavior
```

> ⚠️ **Common mistake:** Using `NATURAL JOIN` in real code. If you add a column with the same name to both tables later (like `created_at`), the join silently adds an extra condition and breaks your query.

---

## Quick reference

| JOIN Type | What it returns | Use case |
|---|---|---|
| `INNER JOIN` | Only rows with a match in both tables | Get orders with customer details |
| `LEFT JOIN` | All left rows + matching right (NULL if none) | Get all customers even without orders |
| `RIGHT JOIN` | All right rows + matching left (NULL if none) | Rare — usually rewrite as LEFT JOIN |
| `FULL OUTER JOIN` | All rows from both, NULLs where no match | Find unmatched rows on either side |
| `CROSS JOIN` | Every row × every row (Cartesian product) | Generating combinations |
| `Self JOIN` | Table joined to itself | Manager/employee hierarchies |

| Syntax | Example |
|---|---|
| `JOIN ... ON a.id = b.a_id` | `INNER JOIN orders ON orders.customer_id = customers.id` |
| `LEFT JOIN ... WHERE b.id IS NULL` | Find rows with no match (unmatched left) |
| `AS alias` | `FROM customers AS c` |
| `table.column` | `SELECT c.name, o.amount` |

---

## Task list
1. The sales report — customer + order join
2. Find the ghosts — customers with no orders
3. The full order receipt — three-table join
4. Employee org chart — self join
5. The complete store report — multi-table with filters

---

## SQL LeetCode
- [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) — 🟢 Easy
- [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) — 🟢 Easy

