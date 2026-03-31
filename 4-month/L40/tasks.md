# L40 Tasks — SQL: DDL, Constraints & Indexes

Complete the tasks below. Run all SQL in `psql`. Save your queries in `.sql` files.

---

## Task 1 — Safe updates — the price adjustment tool

**Scenario**
The product manager at an e-commerce company says: "We need to increase all electronics prices by 8% due to import taxes, cancel all unpaid orders older than 30 days, and update the stock for three specific items after a warehouse count." She emphasizes: "Be careful — a wrong UPDATE once wiped out all our prices with a single query."

**Your task**
- Create `update_practice_db` with a `products` table (id, name, category, price, stock, is_active) — insert 15 products
- Also create an `orders` table (id, product_id, customer, amount, status, created_at)
- Practice the SAFE update workflow for each change:
  1. First: `SELECT name, price FROM products WHERE category = 'Electronics';` — verify the rows
  2. Then: `UPDATE products SET price = ROUND(price * 1.08, 2) WHERE category = 'Electronics' RETURNING name, price;`
  3. Cancel old pending orders: first SELECT to verify, then UPDATE with `RETURNING`
  4. Update stock for 3 specific products using their IDs — use `RETURNING id, name, stock`
  5. Soft-delete (deactivate) all products with stock = 0: `SET is_active = FALSE`
- After all updates, run a final `SELECT` showing before/after would look like for each update

**Expected output** (query 2)
```
-- After price update:
       name        |  old_price  |  new_price
-------------------+-------------+-------------
 Laptop Asus       | 4500000.00  | 4860000.00
 Samsung TV 55"    | 6200000.00  | 6696000.00
 iPhone 15         | 8100000.00  | 8748000.00
(3 rows)
```

**File:** `task_01.sql`

---

## Task 2 — Constraint fortress — a bulletproof orders table

**Scenario**
A junior developer at a logistics startup inserted an order with `amount = -500000` (negative amount), a duplicate tracking number, and a delivery date in the past. All three went in without errors because the table had no constraints. The CFO found the errors during an audit. You have been brought in to add all the necessary constraints.

**Your task**
- Create `logistics_db` with a `shipments` table — start WITHOUT constraints:
  ```sql
  CREATE TABLE shipments (
      id              SERIAL PRIMARY KEY,
      tracking_number VARCHAR(20),
      customer        VARCHAR(100),
      origin_city     VARCHAR(50),
      dest_city       VARCHAR(50),
      weight_kg       NUMERIC(8,2),
      price           NUMERIC(12,2),
      status          VARCHAR(20),
      created_at      TIMESTAMPTZ DEFAULT NOW(),
      delivery_date   DATE
  );
  ```
- First, insert some valid data (5 rows)
- Now add ALL of these constraints using `ALTER TABLE`:
  1. `tracking_number` must be UNIQUE and NOT NULL
  2. `customer` must be NOT NULL
  3. `weight_kg` must be > 0
  4. `price` must be > 0
  5. `status` must be one of: `'pending'`, `'in_transit'`, `'delivered'`, `'returned'`
  6. `delivery_date` must be >= `created_at::date` (delivery can't be in the past)
- After adding constraints, try inserting invalid rows and show the error messages:
  - Negative price → error
  - Duplicate tracking number → error
  - Invalid status → error

**Expected output**
```
-- Attempting: INSERT with price = -1000
ERROR:  new row for relation "shipments" violates check constraint "shipments_price_positive"
DETAIL:  Failing row contains (6, TRK-006, Ahmed, Tashkent, Bukhara, 5.0, -1000, pending, ...)

-- Attempting: duplicate tracking number
ERROR:  duplicate key value violates unique constraint "shipments_tracking_number_key"
```

**File:** `task_02.sql`

---

## Task 3 — Cascade decisions — designing safe foreign keys

**Scenario**
A university database needs to handle cascades carefully. When a student is expelled, their enrollment records should be deleted automatically. But when a course is removed from the catalog, the historical enrollment records must NOT be deleted — they are needed for academic history. Getting the cascade rules wrong has real consequences.

**Your task**
- Create `university_db` with these tables and the correct CASCADE behavior:
  ```sql
  CREATE TABLE students (
      id        SERIAL PRIMARY KEY,
      name      VARCHAR(100) NOT NULL,
      email     VARCHAR(150) UNIQUE NOT NULL,
      status    VARCHAR(20) DEFAULT 'active'
  );

  CREATE TABLE courses (
      id    SERIAL PRIMARY KEY,
      code  VARCHAR(20) UNIQUE NOT NULL,
      title VARCHAR(200) NOT NULL
  );

  CREATE TABLE enrollments (
      id         SERIAL PRIMARY KEY,
      student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
      course_id  INTEGER NOT NULL REFERENCES courses(id) ON DELETE RESTRICT,
      grade      NUMERIC(4,2),
      enrolled_at TIMESTAMPTZ DEFAULT NOW()
  );
  ```
- Insert 3 students, 4 courses, and 8 enrollments (each student enrolled in 2-3 courses)
- Demonstrate CASCADE: delete a student → verify their enrollments are automatically deleted
- Demonstrate RESTRICT: try to delete a course that has enrollments → observe the error
- Add a `UNIQUE` constraint on `(student_id, course_id)` to prevent a student enrolling in the same course twice — test that it works

**Expected output**
```
-- Before deleting student id=1:
SELECT COUNT(*) FROM enrollments WHERE student_id = 1;
 count
-------
     3

-- After DELETE FROM students WHERE id = 1:
SELECT COUNT(*) FROM enrollments WHERE student_id = 1;
 count
-------
     0   ← cascade worked

-- Attempting to delete a course with enrollments:
ERROR:  update or delete on table "courses" violates foreign key constraint
"enrollments_course_id_fkey" on table "enrollments"
```

**File:** `task_03.sql`

---

## Task 4 — Index workshop — before and after performance

**Scenario**
The operations team reports that the order search page in their warehouse app takes 8 seconds to load. The database has 500,000 order records. The senior DBA says: "Run EXPLAIN ANALYZE on the query — I bet there's a Seq Scan on a column with no index." You need to find the bottleneck and fix it.

**Your task**
- Create `warehouse_db` and generate a large dataset (use `generate_series` to insert 100,000 rows):
  ```sql
  -- Insert 100,000 orders using generate_series
  INSERT INTO orders (customer_id, product, amount, status, region, created_at)
  SELECT
      (random() * 999 + 1)::int,
      'Product ' || i,
      (random() * 5000000)::numeric(12,2),
      (ARRAY['pending','shipped','delivered','cancelled'])[floor(random()*4+1)],
      (ARRAY['Tashkent','Samarkand','Bukhara','Namangan','Fergana'])[floor(random()*5+1)],
      NOW() - (random() * INTERVAL '365 days')
  FROM generate_series(1, 100000) AS i;
  ```
- Run `EXPLAIN ANALYZE` on each query BEFORE creating any index — note the execution time and "Seq Scan"
- Create appropriate indexes for each query
- Run `EXPLAIN ANALYZE` AGAIN after indexes — compare the times
  1. `WHERE customer_id = 42`
  2. `WHERE status = 'pending'`
  3. `WHERE region = 'Tashkent' AND status = 'shipped'` → needs composite index
  4. `WHERE created_at >= NOW() - INTERVAL '7 days'`
  5. `WHERE LOWER(product) LIKE 'product 1%'` → needs expression index on `LOWER(product)`

**Expected output**
```
-- BEFORE index:
Seq Scan on orders  (cost=0.00..2891.00 rows=100000) (actual time=0.012..45.821 ms)

-- AFTER index:
Index Scan using idx_orders_customer on orders  (cost=0.29..8.31 rows=1) (actual time=0.052..0.054 ms)
```

**File:** `task_04.sql`

---

## Task 5 — Migration script — version-controlled schema changes

**Scenario**
Kamola just joined a team as the new backend developer. The project has a PostgreSQL database that has been evolving for 6 months. The previous developer just committed changes directly with no migration files — nobody knows the exact current schema. Kamola's first task: create a proper migration system from scratch for the project going forward.

**Your task**
- Create a `migrations` table to track applied migrations:
  ```sql
  CREATE TABLE schema_migrations (
      id          SERIAL PRIMARY KEY,
      version     VARCHAR(20) UNIQUE NOT NULL,
      description TEXT NOT NULL,
      applied_at  TIMESTAMPTZ DEFAULT NOW()
  );
  ```
- Write 3 migration files as separate SQL blocks (in the same `.sql` file, separated by comments):

  **Migration 001 — Create users table**
  ```sql
  -- UP
  CREATE TABLE users (
      id         SERIAL PRIMARY KEY,
      username   VARCHAR(50) UNIQUE NOT NULL,
      email      VARCHAR(150) UNIQUE NOT NULL,
      created_at TIMESTAMPTZ DEFAULT NOW()
  );
  INSERT INTO schema_migrations (version, description)
  VALUES ('001', 'Create users table');

  -- DOWN
  DROP TABLE IF EXISTS users;
  DELETE FROM schema_migrations WHERE version = '001';
  ```

  **Migration 002 — Add profile fields to users**
  - Add columns: `full_name VARCHAR(100)`, `phone VARCHAR(20)`, `is_active BOOLEAN DEFAULT TRUE`
  - Record it in `schema_migrations`
  - Write the DOWN migration to remove these columns

  **Migration 003 — Create posts table with FK to users**
  - Create a `posts` table with id, user_id (FK with ON DELETE CASCADE), title, body, created_at
  - Add an index on `user_id`
  - Record in `schema_migrations`
  - Write the DOWN migration

- After running all 3 UP migrations, query `schema_migrations` to confirm all are recorded
- Run the DOWN migration for 003 and verify the posts table is gone

**Expected output**
```
SELECT * FROM schema_migrations;
 id | version |          description           |         applied_at
----+---------+--------------------------------+----------------------------
  1 | 001     | Create users table             | 2025-01-15 10:23:41+05
  2 | 002     | Add profile fields to users    | 2025-01-15 10:23:41+05
  3 | 003     | Create posts table with FK     | 2025-01-15 10:23:41+05
(3 rows)
```

**File:** `task_05.sql`

