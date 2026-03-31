# L37 Tasks — SQL: SELECT, Filtering & Sorting

Complete the tasks below. Run all SQL in `psql`. Save your queries in `.sql` files.

---

## Task 1 — Product catalog queries — the online store

**Scenario**
Feruza manages the backend of an online electronics store. The marketing team keeps asking her for filtered product lists: "Show me all laptops under 5 million, sorted by price." She needs to write clean SELECT queries to answer these requests without modifying any data.

**Your task**
- Create database `electronics_db` and a `products` table:
  ```sql
  CREATE TABLE products (
      id         SERIAL PRIMARY KEY,
      name       VARCHAR(200) NOT NULL,
      category   VARCHAR(50)  NOT NULL,
      brand      VARCHAR(100),
      price      NUMERIC(12,2) NOT NULL,
      stock      INTEGER DEFAULT 0,
      rating     NUMERIC(3,2),
      created_at TIMESTAMPTZ DEFAULT NOW()
  );
  ```
- Insert at least 12 products across categories: `'Laptop'`, `'Phone'`, `'Tablet'`, `'Accessory'` — vary prices, some with NULL rating, some with stock = 0
- Write and run these queries:
  1. All products, showing only `name`, `brand`, `price` — ordered by price ascending
  2. All laptops under 5,000,000 sum, ordered by price
  3. All products with stock = 0 (out of stock)
  4. Products with rating >= 4.0 ordered by rating DESC
  5. Products where brand is NULL (no brand set)
  6. Products where category is either `'Phone'` or `'Tablet'` — using `IN`
  7. Top 5 most expensive products

**Expected output** (query 7 example)
```
      name       |   price
-----------------+-----------
 Gaming Laptop   | 12500000.00
 MacBook Pro     | 11800000.00
 iPad Pro        |  5900000.00
 Samsung S24     |  4200000.00
 Dell XPS        |  3800000.00
(5 rows)
```

**File:** `task_01.sql`

---

## Task 2 — Order search & filtering — the operations dashboard

**Scenario**
Otabek works in operations at a logistics company. Every morning he opens the order dashboard to find: pending orders, high-value shipments, and orders placed in the last 7 days. He's tired of scrolling — he wants SQL that finds exactly what he needs instantly.

**Your task**
- Create `logistics_db` with an `orders` table:
  ```sql
  CREATE TABLE orders (
      id           SERIAL PRIMARY KEY,
      customer     VARCHAR(100) NOT NULL,
      destination  VARCHAR(100) NOT NULL,
      weight_kg    NUMERIC(8,2),
      total_price  NUMERIC(12,2) NOT NULL,
      status       VARCHAR(20) DEFAULT 'pending',
      created_at   TIMESTAMPTZ DEFAULT NOW()
  );
  ```
- Insert 15 orders with varied statuses (`'pending'`, `'shipped'`, `'delivered'`, `'cancelled'`), destinations, and prices
- Write these queries:
  1. All pending orders, newest first
  2. All orders to `'Samarkand'` or `'Bukhara'`
  3. Orders with `total_price` between 500,000 and 2,000,000
  4. Orders that are NOT cancelled or delivered (active orders)
  5. Orders where `weight_kg` is NULL (weight not recorded yet)
  6. Orders created in the last 7 days: `WHERE created_at >= NOW() - INTERVAL '7 days'`
  7. Count of orders by status (preview of next lesson — try: `SELECT status, COUNT(*) FROM orders GROUP BY status`)

**Expected output** (query 4 example)
```
 id | customer        | status  | total_price
----+-----------------+---------+-------------
  1 | Alisher Karimov | pending |   850000.00
  3 | Zulfiya Norova  | shipped |  1200000.00
  7 | Bobur Toshev    | pending |   340000.00
(3 rows)
```

**File:** `task_02.sql`

---

## Task 3 — Customer directory — sorted and paginated

**Scenario**
The admin panel of a CRM system needs a "customer directory" page that shows customers sorted alphabetically, 10 per page. The product manager also wants: "a search bar that finds customers by name or email." You need to build the queries that power this.

**Your task**
- Create `crm_db` with a `customers` table:
  ```sql
  CREATE TABLE customers (
      id           SERIAL PRIMARY KEY,
      full_name    VARCHAR(100) NOT NULL,
      email        VARCHAR(150) UNIQUE NOT NULL,
      phone        VARCHAR(20),
      city         VARCHAR(50),
      loyalty_tier VARCHAR(20) DEFAULT 'standard',
      joined_at    TIMESTAMPTZ DEFAULT NOW()
  );
  ```
- Insert 25 customers from various Uzbekistan cities, with varied loyalty tiers: `'standard'`, `'silver'`, `'gold'`, `'platinum'`
- Write these queries:
  1. Page 1: first 10 customers, alphabetically by `full_name`
  2. Page 2: customers 11–20, same ordering
  3. Search: customers whose name contains `'ov'` (case-insensitive using `ILIKE`)
  4. All customers from `'Tashkent'`, sorted by `joined_at` newest first
  5. All gold or platinum customers, ordered by name
  6. Customers with no phone number on file
  7. Show `full_name`, `city`, and `UPPER(loyalty_tier) AS tier` for all customers

**Expected output** (query 1 example)
```
    full_name          |       email         |   city
-----------------------+---------------------+-----------
 Abdullayev Jasur      | jasur@mail.com      | Tashkent
 Alijonova Maftuna     | maftuna@mail.com    | Namangan
 ...
(10 rows)
```

**File:** `task_03.sql`

---

## Task 4 — Inventory status report — CASE WHEN

**Scenario**
The warehouse manager at a pharmacy chain needs a daily inventory report. She doesn't want raw numbers — she wants each medicine classified as `'Critical'`, `'Low'`, `'Adequate'`, or `'Overstocked'` so her team knows exactly what to reorder without manually checking each row.

**Your task**
- Create `pharmacy_db` with a `medicines` table:
  ```sql
  CREATE TABLE medicines (
      id          SERIAL PRIMARY KEY,
      name        VARCHAR(150) NOT NULL,
      category    VARCHAR(50),
      stock_units INTEGER NOT NULL DEFAULT 0,
      unit_price  NUMERIC(10,2) NOT NULL,
      supplier    VARCHAR(100)
  );
  ```
- Insert 15 medicines with varied stock levels (some at 0, some very high)
- Write a single query that shows:
  - `name`, `category`, `stock_units`
  - A `stock_status` column using `CASE WHEN`:
    - 0 units → `'CRITICAL - Out of stock'`
    - 1–20 units → `'LOW - Reorder now'`
    - 21–100 units → `'Adequate'`
    - Over 100 → `'Overstocked'`
  - A `total_value` column: `stock_units * unit_price`
  - A `price_tier` column: under 5,000 → `'Cheap'`, 5,000–50,000 → `'Standard'`, over 50,000 → `'Expensive'`
- Order by `stock_units ASC` so critical items appear first

**Expected output**
```
       name        | stock_units |       stock_status        | total_value | price_tier
-------------------+-------------+---------------------------+-------------+------------
 Paracetamol 500mg |           0 | CRITICAL - Out of stock   |        0.00 | Cheap
 Ibuprofen 200mg   |           5 | LOW - Reorder now         |     5500.00 | Cheap
 Amoxicillin 500mg |          18 | LOW - Reorder now         |    90000.00 | Standard
 Vitamin C 1000mg  |          45 | Adequate                  |    67500.00 | Standard
```

**File:** `task_04.sql`

---

## Task 5 — String & null cleanup — the data quality audit

**Scenario**
A company imported 3 years of customer data from an old Excel system into PostgreSQL. The data is messy: some emails are uppercase, some names have extra spaces, some phone numbers are missing. The data team asks you to write queries that identify and report all data quality problems — without modifying the data yet.

**Your task**
- Use the `customers` table from Task 3 (or recreate it with messy data — intentionally insert some rows with NULL phone, inconsistent city casing like `'tashkent'` vs `'Tashkent'`, extra spaces in names)
- Write these data audit queries:
  1. Find all customers with missing phone: `WHERE phone IS NULL`
  2. Find duplicate emails (hint: `GROUP BY email HAVING COUNT(*) > 1`)
  3. Show all customer names with length over 50 characters
  4. Show `full_name` trimmed and lowercased: `LOWER(TRIM(full_name)) AS clean_name`
  5. Show customers where `LOWER(city) = 'tashkent'` — this catches mixed-case entries
  6. Show the `COALESCE(phone, 'MISSING')` for all customers — replace NULL with text
  7. Show `CONCAT(full_name, ' <', email, '>')` as a formatted contact string — like `"Sardor Toshev <sardor@mail.com>"`

**Expected output** (query 7 example)
```
           contact_string
--------------------------------------
 Abdullayev Jasur <jasur@mail.com>
 Alijonova Maftuna <maftuna@mail.com>
 Sardor Toshev <sardor@mail.com>
```

**File:** `task_05.sql`

