# L38 Tasks — SQL: JOINs & Relationships

Complete the tasks below. Run all SQL in `psql`. Save your queries in `.sql` files.

---

## Task 1 — The sales report — customer + order join

**Scenario**
The sales manager at an online store wants a daily report showing every order alongside the full customer name and email — not just a customer ID number. Without a JOIN, she would have to cross-reference two tables manually for hundreds of orders.

**Your task**
- Create database `store_db` with these tables and insert realistic data:
  ```sql
  CREATE TABLE customers (
      id         SERIAL PRIMARY KEY,
      full_name  VARCHAR(100) NOT NULL,
      email      VARCHAR(150) UNIQUE NOT NULL,
      city       VARCHAR(50)
  );

  CREATE TABLE orders (
      id           SERIAL PRIMARY KEY,
      customer_id  INTEGER NOT NULL REFERENCES customers(id),
      product      VARCHAR(200) NOT NULL,
      amount       NUMERIC(12,2) NOT NULL,
      status       VARCHAR(20) DEFAULT 'pending',
      ordered_at   TIMESTAMPTZ DEFAULT NOW()
  );
  ```
- Insert 5 customers and at least 10 orders (some customers have multiple orders, at least one customer has no orders)
- Write these JOIN queries:
  1. All orders with customer full name and email (INNER JOIN)
  2. Orders over 500,000 sum, with customer name, sorted by amount DESC
  3. Count of orders per customer: `SELECT c.full_name, COUNT(o.id) AS order_count`
  4. Total amount spent per customer, sorted highest first
  5. All completed orders with customer email (for sending confirmation)

**Expected output** (query 1 example)
```
    full_name      |       email        |    product    |  amount
-------------------+--------------------+---------------+---------
 Nilufar Karimova  | nilufar@mail.com   | Laptop HP     | 4500000
 Nilufar Karimova  | nilufar@mail.com   | USB Hub       |   85000
 Sardor Toshmatov  | sardor@mail.com    | iPhone 15     | 8200000
(10 rows)
```

**File:** `task_01.sql`

---

## Task 2 — Find the ghosts — customers with no orders

**Scenario**
The marketing team at a subscription service wants to run a "win-back" email campaign targeting users who registered but never made a purchase. They need a list of these "ghost" customers — signed up but never ordered.

**Your task**
- Use the `store_db` from Task 1
- Write a query using `LEFT JOIN` + `WHERE o.id IS NULL` to find all customers who have **never** placed an order
- Show their `full_name`, `email`, and `city`
- Also write a query that finds orders referencing a `customer_id` that doesn't exist in the customers table (use `RIGHT JOIN` or `FULL OUTER JOIN`)
- Show the count of ghost customers: `SELECT COUNT(*) FROM ...`
- Modify the first query to also show customers who have ordered but all their orders are `'cancelled'` (LEFT JOIN, filter for only cancelled or no orders)

**Expected output**
```
-- Ghost customers (never ordered)
    full_name      |       email         |   city
-------------------+---------------------+-----------
 Malika Yusupova   | malika@mail.com     | Samarkand
(1 row)

-- Count
 count
-------
     1
```

**File:** `task_02.sql`

---

## Task 3 — The full order receipt — three-table join

**Scenario**
An e-commerce company needs to generate order receipts. Each receipt must show: the customer's name and email, the ordered products (with category and price each), the quantity, and the line total. This requires joining customers → orders → order_items → products in one query.

**Your task**
- Create these additional tables in `store_db`:
  ```sql
  CREATE TABLE products (
      id        SERIAL PRIMARY KEY,
      name      VARCHAR(200) NOT NULL,
      category  VARCHAR(50),
      price     NUMERIC(12,2) NOT NULL
  );

  CREATE TABLE order_items (
      id          SERIAL PRIMARY KEY,
      order_id    INTEGER NOT NULL REFERENCES orders(id),
      product_id  INTEGER NOT NULL REFERENCES products(id),
      quantity    INTEGER NOT NULL CHECK (quantity > 0)
  );
  ```
- Insert 6 products and create 3 orders with multiple items each
- Write a single query that returns:
  - `c.full_name` as customer
  - `o.id` as order_id
  - `p.name` as product
  - `p.category`
  - `oi.quantity`
  - `p.price`
  - `oi.quantity * p.price` as line_total
- Filter to show only one specific `order_id`
- Then write a second query: total value of each order (SUM of all line totals, grouped by `o.id`)

**Expected output**
```
  customer      | order_id |    product    | category | qty |   price  | line_total
----------------+----------+---------------+----------+-----+----------+-----------
 Sardor Toshev  |        2 | Keyboard      | Accessor |   2 | 120000   |   240000
 Sardor Toshev  |        2 | Mouse Logitech| Accessor |   1 |  85000   |    85000
 Sardor Toshev  |        2 | Monitor 24"   | Display  |   1 |1200000   |  1200000
(3 rows)

-- Total per order
 order_id | order_total
----------+-------------
        1 |  4585000.00
        2 |  1525000.00
        3 |   340000.00
```

**File:** `task_03.sql`

---

## Task 4 — Employee org chart — self join

**Scenario**
A company's HR system stores all employees in one table. Every employee (except the CEO) has a `manager_id` pointing to another row in the same table. HR wants a report showing each employee's name alongside their manager's name — and wants to flag employees whose salary is higher than their manager's.

**Your task**
- Create `hr_db` with an `employees` table:
  ```sql
  CREATE TABLE employees (
      id          SERIAL PRIMARY KEY,
      name        VARCHAR(100) NOT NULL,
      department  VARCHAR(50),
      salary      NUMERIC(12,2) NOT NULL,
      manager_id  INTEGER REFERENCES employees(id)  -- NULL for the CEO
  );
  ```
- Insert 10 employees: 1 CEO (no manager), 3 managers reporting to CEO, 6 staff reporting to managers
- Write these self-join queries:
  1. Show every employee with their manager's name (`LEFT JOIN` so CEO appears with `NULL` manager)
  2. Show only employees who earn more than their own manager
  3. Show the full chain: employee → manager → manager's manager (3-level join using 3 aliases)
  4. Count direct reports per manager: how many employees report to each manager

**Expected output** (query 1)
```
      employee      | department |  salary   |  manager
--------------------+------------+-----------+-----------
 Kamol Tursunov     | CEO        | 25000000  | (null)
 Aziz Rahimov       | Engineering| 15000000  | Kamol Tursunov
 Gulnora Hasanova   | Marketing  | 12000000  | Kamol Tursunov
 Jasur Mirzayev     | Engineering|  8000000  | Aziz Rahimov
```

**File:** `task_04.sql`

---

## Task 5 — The complete store report — multi-table with filters

**Scenario**
At month-end, the CEO of the store wants one comprehensive report: "Show me all completed orders from this month, with the customer's city, the products ordered, quantities, and total order value. Sort by total order value, highest first. I only want orders above 500,000 sum total."

**Your task**
- Use all tables from Tasks 1 and 3 in `store_db`
- Write a single query that:
  - Joins `customers`, `orders`, `order_items`, and `products`
  - Filters: `o.status = 'completed'` AND order was placed this month
  - Groups by `o.id`, `c.full_name`, `c.city`
  - Calculates `SUM(oi.quantity * p.price) AS order_total`
  - Filters groups: `HAVING SUM(oi.quantity * p.price) > 500000`
  - Orders by `order_total DESC`
- Also write a simpler summary: total revenue this month, total number of completed orders, and average order value

**Expected output**
```
  customer_name   |  city   | order_id | order_total
------------------+---------+----------+-------------
 Sardor Toshmatov | Tashkent|        3 |  5200000.00
 Nilufar Karimova | Bukhara |        1 |  4585000.00
(2 rows)

-- Summary
 total_revenue | completed_orders | avg_order_value
---------------+------------------+-----------------
   9785000.00  |                2 |      4892500.00
```

**File:** `task_05.sql`

