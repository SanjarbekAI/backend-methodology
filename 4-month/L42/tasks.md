# L42 Tasks — Advanced Queries & Transactions

Complete the tasks below. Run SQL in `psql` and Python tasks in `.py` files.

---

## Task 1 — The bank transfer — transactions in action

**Scenario**
A fintech startup is building a peer-to-peer payment feature. The CTO says: "Every transfer must be atomic — if we debit one account and then the server crashes before crediting the other, we've just stolen someone's money." You need to implement the transaction correctly and demonstrate both the success and failure paths.

**Your task**
- Create `bank_db` with an `accounts` table (id, owner_name, balance NUMERIC, created_at) and a `transfer_log` table (id, from_id, to_id, amount, status, transferred_at)
- Insert 4 accounts with different balances
- Write these transaction demonstrations in SQL:
  1. **Successful transfer:** BEGIN → debit account 1 → credit account 2 → insert into transfer_log → COMMIT. Show balances before and after.
  2. **Failed transfer (insufficient funds):** BEGIN → check balance → if insufficient, INSERT into transfer_log with `status='failed'` → ROLLBACK. Show that account balances did NOT change.
  3. **SAVEPOINT demo:** BEGIN → update account 1 → SAVEPOINT sp1 → update account 2 (intentionally wrong ID) → ROLLBACK TO sp1 → try with correct ID → COMMIT.
- After all demos, run `SELECT * FROM accounts ORDER BY id` and `SELECT * FROM transfer_log` to verify the state

**Expected output**
```
-- Before transfer:
 id | owner   | balance
----+---------+----------
  1 | Sardor  | 5000000
  2 | Nilufar | 2000000

-- After successful transfer of 1000000:
 id | owner   | balance
----+---------+----------
  1 | Sardor  | 4000000
  2 | Nilufar | 3000000

-- transfer_log:
 from_id | to_id | amount  | status
---------+-------+---------+----------
       1 |     2 | 1000000 | completed
       1 |     3 | 9999999 | failed       ← rollback: balances unchanged
```

**File:** `task_01.sql`

---

## Task 2 — Sales leaderboard — window functions

**Scenario**
The sales director at an insurance company wants a leaderboard: rank all agents by total sales this month, show their rank within their regional office, flag the top 3 company-wide, and compare each agent's sales to the regional average.

**Your task**
- Create `sales_db` with `agents` (id, name, region, hire_date) and `sales` (id, agent_id, amount, sold_at)
- Insert 10 agents across 3 regions, 50 sales records
- Write these window function queries:
  1. Rank all agents by total sales, company-wide (use `DENSE_RANK()`)
  2. Rank agents within each region (`PARTITION BY region`)
  3. Show each agent's sales, regional total, and their % contribution to the region:
     ```sql
     SUM(total) OVER (PARTITION BY region) AS region_total,
     ROUND(total * 100.0 / SUM(total) OVER (PARTITION BY region), 1) AS pct_of_region
     ```
  4. Show the top-earning agent in each region using `FIRST_VALUE()`
  5. Use a CTE with `DENSE_RANK()` to return ONLY the top 3 agents company-wide

**Expected output** (query 2)
```
     agent     |  region   | total_sales | region_rank
---------------+-----------+-------------+-------------
 Kamol Tursunov| Tashkent  |  12500000   |           1
 Aziz Rahimov  | Tashkent  |   8400000   |           2
 Lola Mirzayeva| Samarkand |  11200000   |           1
 Bobur Alimov  | Samarkand |   7800000   |           2
```

**File:** `task_02.sql`

---

## Task 3 — Monthly trend analyzer — LAG and running totals

**Scenario**
The CFO of a subscription SaaS company needs a monthly revenue report that shows: this month's revenue, last month's revenue, the change (absolute and percentage), and the cumulative revenue since the company launched. Without LAG(), this would require joining the table to itself for every month.

**Your task**
- Use or create a `monthly_revenue` table (month DATE, revenue NUMERIC, new_customers INT, churned_customers INT)
- Insert 12 months of data
- Write these window queries:
  1. Month, revenue, previous month revenue (`LAG`), and month-over-month change:
     ```sql
     LAG(revenue) OVER (ORDER BY month) AS prev_revenue,
     revenue - LAG(revenue) OVER (ORDER BY month) AS change
     ```
  2. Month-over-month percentage change:
     `ROUND((revenue - LAG(revenue) OVER (...)) / LAG(revenue) OVER (...) * 100, 1) AS pct_change`
  3. Cumulative revenue (running total):
     `SUM(revenue) OVER (ORDER BY month ROWS UNBOUNDED PRECEDING) AS cumulative`
  4. 3-month moving average of revenue
  5. Net customer change per month and running total of customer base

**Expected output** (query 1–3 combined)
```
   month    |  revenue   | prev_revenue |  change   | cumulative
------------+------------+--------------+-----------+-----------
 2024-01-01 |  8500000   |         null |      null |   8500000
 2024-02-01 |  9200000   |    8500000   |   700000  |  17700000
 2024-03-01 | 11500000   |    9200000   |  2300000  |  29200000
 2024-04-01 | 10800000   |   11500000   |  -700000  |  40000000
```

**File:** `task_03.sql`

---

## Task 4 — The order dashboard view — creating useful views

**Scenario**
The customer support team at an e-commerce company constantly queries the same complex JOIN: order details + customer info + product list + totals. The query is 25 lines long and every support agent writes it slightly differently — causing inconsistencies. The solution: create a VIEW that the whole team can query like a simple table.

**Your task**
- Use `store_db` from L38 (or recreate it with customers, orders, order_items, products tables)
- Create these views:
  1. `order_summary` — one row per order with: order_id, customer_name, email, item_count, order_total, status, ordered_at
  2. `product_performance` — one row per product with: product_id, product_name, category, times_ordered, total_qty_sold, total_revenue
  3. `customer_profile` — one row per customer with: customer_id, name, email, city, total_orders, total_spent, last_order_date, loyalty_tier (CASE WHEN on total_spent)
- Demonstrate using these views:
  ```sql
  SELECT * FROM order_summary WHERE status = 'pending';
  SELECT * FROM product_performance ORDER BY total_revenue DESC LIMIT 5;
  SELECT * FROM customer_profile WHERE loyalty_tier = 'Gold';
  ```
- Show the view definition with `\d+ order_summary` in psql

**Expected output**
```
-- customer_profile view
  name           | total_orders | total_spent  | loyalty_tier
-----------------+--------------+--------------+--------------
 Sardor Toshmatov|            8 | 18500000.00  | Gold
 Nilufar Karimova|            5 | 12300000.00  | Silver
 Malika Yusupova |            2 |  1850000.00  | Standard
```

**File:** `task_04.sql`

---

## Task 5 — Full transaction app — Python + multi-step transactions

**Scenario**
You are building the order placement system for an online store. Placing an order is a multi-step transaction: (1) check product stock, (2) create the order record, (3) insert order items, (4) reduce stock for each item, (5) log the event. If ANY step fails, the entire order must be rolled back — no partial orders, no phantom stock reductions.

**Your task**
- Use `store_db` with products, customers, orders, order_items tables
- Write `task_05.py` with a `place_order(conn, customer_id, items: list[dict])` function where `items = [{"product_id": 1, "quantity": 2}, ...]`
- The function must:
  1. Check stock for ALL items FIRST — if any is insufficient, raise a custom exception before touching anything
  2. Begin a transaction
  3. Create the order record (`INSERT INTO orders ... RETURNING id`)
  4. For each item: insert into `order_items`, then `UPDATE products SET stock = stock - quantity`
  5. If all succeed: `conn.commit()` and return the order id
  6. On ANY exception: `conn.rollback()` and re-raise with a clear message
- Write a `main()` that:
  - Places a successful order and prints the confirmation
  - Attempts an order with insufficient stock and shows the graceful error
  - Attempts an order with an invalid product_id (non-existent) and shows the error
  - After all attempts, queries `orders` and `products` to prove the database is consistent

**Expected output**
```
Placing order for customer 1: [{'product_id': 2, 'quantity': 1}, {'product_id': 5, 'quantity': 3}]
✓ Order #12 placed successfully! Total: 4,850,000 sum

Placing order for customer 2: [{'product_id': 3, 'quantity': 100}]
✗ Order failed: Insufficient stock for "Laptop HP" (requested: 100, available: 5)
  Database rolled back — no changes made.

Placing order with invalid product: [{'product_id': 9999, 'quantity': 1}]
✗ Order failed: Product ID 9999 does not exist.
  Database rolled back — no changes made.
```

**File:** `task_05.py`

