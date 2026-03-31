# L39 Tasks — SQL: Aggregations, GROUP BY & Subqueries

Complete the tasks below. Run all SQL in `psql`. Save your queries in `.sql` files.

---

## Task 1 — Revenue dashboard — aggregations across a store

**Scenario**
The CEO of an online store opens her dashboard every Monday morning and asks the same questions: "How many orders did we get? What's our total revenue? What's the biggest and smallest order? What percentage of orders are completed?" You are the backend developer who builds the queries that power this dashboard.

**Your task**
- Create `analytics_db` and populate it with these tables (insert at least 20 orders with varied statuses and amounts):
  ```sql
  CREATE TABLE customers (id SERIAL PRIMARY KEY, name VARCHAR(100), city VARCHAR(50));
  CREATE TABLE orders (
      id           SERIAL PRIMARY KEY,
      customer_id  INTEGER REFERENCES customers(id),
      amount       NUMERIC(12,2),
      status       VARCHAR(20),
      ordered_at   TIMESTAMPTZ DEFAULT NOW()
  );
  ```
- Write these queries:
  1. Total number of orders and total revenue (all statuses)
  2. Total revenue from completed orders only
  3. Min, max, and average order amount (all completed orders)
  4. Count of orders per status
  5. Revenue and order count for TODAY only: `WHERE ordered_at::date = CURRENT_DATE`
  6. Percentage of orders that are completed:
     ```sql
     SELECT
         ROUND(COUNT(*) FILTER (WHERE status = 'completed') * 100.0 / COUNT(*), 1)
         AS completion_rate_pct
     FROM orders;
     ```

**Expected output** (query 4)
```
   status    | order_count
-------------+-------------
 completed   |          12
 pending     |           5
 cancelled   |           2
 shipped     |           1
(4 rows)
```

**File:** `task_01.sql`

---

## Task 2 — Top performers — GROUP BY with HAVING

**Scenario**
The regional director of a pharmacy chain needs to identify the top-performing branches (by total sales), flag products that are selling faster than 50 units per month, and find customers who have made more than 3 purchases. This all comes from one database with aggregation queries.

**Your task**
- Create `pharmacy_analytics_db` with:
  ```sql
  CREATE TABLE branches (id SERIAL PRIMARY KEY, name VARCHAR(100), city VARCHAR(50));
  CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR(150), category VARCHAR(50), price NUMERIC(10,2));
  CREATE TABLE sales (
      id          SERIAL PRIMARY KEY,
      branch_id   INTEGER REFERENCES branches(id),
      product_id  INTEGER REFERENCES products(id),
      customer    VARCHAR(100),
      quantity    INTEGER,
      sold_at     TIMESTAMPTZ DEFAULT NOW()
  );
  ```
- Insert 5 branches, 10 products, 40 sales records
- Write these GROUP BY + HAVING queries:
  1. Total sales value per branch, only branches above 2,000,000 sum total
  2. Total quantity sold per product — top 5 products by quantity
  3. Customers who made more than 3 purchases (group by customer name)
  4. Average sale value per city — only cities with average above 100,000
  5. Products sold in more than one branch (distinct branch count > 1)

**Expected output** (query 1)
```
   branch_name    |  city   | total_sales
------------------+---------+-------------
 Meridian Pharmacy| Tashkent| 8450000.00
 CityMed          | Tashkent| 3200000.00
(2 rows)
```

**File:** `task_02.sql`

---

## Task 3 — Monthly trend report — GROUP BY with dates

**Scenario**
The finance team at a telecom company wants to see monthly revenue trends for the past year. They also want a weekly breakdown of new customer registrations. The data team needs queries that group by time periods automatically — not manually for each month.

**Your task**
- Use `analytics_db` from Task 1 (or extend with more historical data — insert orders with different `ordered_at` timestamps spanning several months)
- Write these time-based GROUP BY queries:
  1. Total revenue per month using `DATE_TRUNC('month', ordered_at)`:
     ```sql
     SELECT DATE_TRUNC('month', ordered_at) AS month, SUM(amount) AS monthly_revenue
     FROM orders GROUP BY month ORDER BY month;
     ```
  2. Count of orders per day of week: `EXTRACT(DOW FROM ordered_at)` (0=Sunday, 6=Saturday)
  3. Revenue per month for completed orders only, last 6 months:
     `WHERE ordered_at >= NOW() - INTERVAL '6 months'`
  4. Monthly average order value — show months where avg is above overall average (subquery inside HAVING)
  5. Running total: use a subquery to show each month's revenue AND cumulative revenue up to that month

**Expected output** (query 1)
```
         month          | monthly_revenue
------------------------+-----------------
 2024-10-01 00:00:00+05 |     12500000.00
 2024-11-01 00:00:00+05 |      9800000.00
 2024-12-01 00:00:00+05 |     15200000.00
 2025-01-01 00:00:00+05 |      8400000.00
(4 rows)
```

**File:** `task_03.sql`

---

## Task 4 — Smart filtering — subqueries in WHERE

**Scenario**
The product manager at an electronics store wants specific filtered views that are too complex for a simple WHERE clause: "Show me products that are more expensive than our average product price." "Show me customers who have made at least one order over 1,000,000 sum." "Show me products that have never been ordered." These require subqueries.

**Your task**
- Use `store_db` from L38 tasks (or recreate with products, customers, orders tables)
- Write these subquery-based queries:
  1. Products priced above the average price:
     `WHERE price > (SELECT AVG(price) FROM products)`
  2. Customers who have placed at least one order over 1,000,000:
     `WHERE id IN (SELECT customer_id FROM orders WHERE amount > 1000000)`
  3. Products that have NEVER been ordered (use `NOT IN` or `NOT EXISTS`):
     `WHERE id NOT IN (SELECT DISTINCT product_id FROM order_items)`
  4. The single most expensive product in each category (correlated subquery):
     ```sql
     WHERE price = (
         SELECT MAX(price) FROM products p2 WHERE p2.category = products.category
     )
     ```
  5. Customers whose total spending exceeds the average total spending per customer (two-level subquery or CTE)

**Expected output** (query 3)
```
-- Products never ordered
      name       | category | price
-----------------+----------+--------
 HDMI Cable 2m   | Accessor | 25000
 Screen Protector| Accessor | 15000
(2 rows)
```

**File:** `task_04.sql`

---

## Task 5 — Executive summary — CTEs with multi-step logic

**Scenario**
The COO asks for a monthly executive report combining multiple metrics: top 3 customers by revenue, revenue by product category, and a summary line comparing this month to last month. The query logic is too complex for nested subqueries — you need CTEs.

**Your task**
- Use your `store_db` or `analytics_db`
- Build this multi-step report using CTEs:
  ```sql
  WITH
  -- Step 1: total spending per customer
  customer_totals AS (
      SELECT c.id, c.full_name, c.city, SUM(o.amount) AS total_spent
      FROM customers c
      INNER JOIN orders o ON c.id = o.customer_id
      WHERE o.status = 'completed'
      GROUP BY c.id, c.full_name, c.city
  ),
  -- Step 2: rank customers by spending
  ranked_customers AS (
      SELECT *, RANK() OVER (ORDER BY total_spent DESC) AS spending_rank
      FROM customer_totals
  )
  -- Step 3: return only top 3
  SELECT full_name, city, total_spent, spending_rank
  FROM ranked_customers
  WHERE spending_rank <= 3;
  ```
- Write a second CTE query: revenue by category this month vs last month side by side
- Write a third CTE query: find customers who placed orders in 2 or more different months (loyal customers)

**Expected output** (first CTE query)
```
    full_name      |   city   | total_spent | spending_rank
-------------------+----------+-------------+---------------
 Sardor Toshmatov  | Tashkent | 18500000.00 |             1
 Nilufar Karimova  | Bukhara  | 12300000.00 |             2
 Malika Yusupova   | Namangan |  8900000.00 |             3
(3 rows)
```

**File:** `task_05.sql`

