# L36 Tasks — Relational Databases & PostgreSQL Intro

Complete the tasks below. Open `psql` in your terminal and run the SQL commands there. Save your SQL commands in `.sql` files as your submission.

---

## Task 1 — PostgreSQL installation & first connection

**Scenario**
Aziz just joined a backend team. His first task before writing a single line of code: install PostgreSQL and prove he can connect to it. His team lead says: "Send me a screenshot of `psql` showing our dev database exists."

**Your task**
- Install PostgreSQL on your machine (if not already installed)
- Start the PostgreSQL service
- Connect to PostgreSQL using `psql -U postgres`
- Run `\l` and observe the default databases
- Create a new database called `devdb`:
  ```sql
  CREATE DATABASE devdb;
  ```
- Create a new user:
  ```sql
  CREATE USER devuser WITH PASSWORD 'dev1234';
  GRANT ALL PRIVILEGES ON DATABASE devdb TO devuser;
  ```
- Exit and reconnect as `devuser`:
  ```bash
  psql -U devuser -d devdb
  ```
- Run `\conninfo` inside psql — note what it shows
- Run `SELECT version();` and observe the PostgreSQL version output

**Expected output**
```
devdb=# \conninfo
You are connected to database "devdb" as user "devuser" via socket in ...

devdb=# SELECT version();
                           version
--------------------------------------------------------------
 PostgreSQL 15.x on x86_64-pc-linux-gnu, compiled by gcc ...
```

**File:** `task_01.sql` (paste all the SQL commands you ran)

---

## Task 2 — Create the coffee shop database

**Scenario**
Lola is opening a small coffee shop and wants to track her menu items and daily sales digitally. She hired you to set up the database. She needs two tables: one for menu items and one for sales records.

**Your task**
- Connect to `devdb` (or create a new database `coffee_db`)
- Create a `menu_items` table with these columns:
  - `id` — auto-increment primary key
  - `name` — required, max 100 characters
  - `category` — required (e.g., `'Hot Drinks'`, `'Cold Drinks'`, `'Food'`)
  - `price` — exact decimal, required
  - `available` — boolean, default `TRUE`
- Create a `sales` table with:
  - `id` — auto-increment primary key
  - `item_id` — foreign key referencing `menu_items(id)`
  - `quantity` — integer, required, must be positive (use `CHECK (quantity > 0)`)
  - `sold_at` — timestamp, default current time
  - `cashier_name` — max 50 chars, required
- Run `\dt` to confirm both tables exist
- Run `\d menu_items` and `\d sales` to show their structures

**Expected output**
```
coffee_db=# \dt
        List of relations
 Schema |    Name    | Type  |  Owner
--------+------------+-------+---------
 public | menu_items | table | devuser
 public | sales      | table | devuser

coffee_db=# \d sales
                         Table "public.sales"
    Column     |            Type             | Nullable |      Default
---------------+-----------------------------+----------+--------------------
 id            | integer                     | not null | nextval('sales_id_seq')
 item_id       | integer                     | not null |
 quantity      | integer                     | not null |
 sold_at       | timestamp with time zone    |          | now()
 cashier_name  | character varying(50)       | not null |
```

**File:** `task_02.sql`

---

## Task 3 — Design the library database

**Scenario**
The city library is replacing their paper catalog with a digital system. The librarian explains: "We need to track our books, our members, and which member has borrowed which book." You need to design the schema from scratch.

**Your task**
- Create a database `library_db`
- Design and create these 3 tables:

  **`books`**
  - `id` SERIAL PRIMARY KEY
  - `title` VARCHAR(200) NOT NULL
  - `author` VARCHAR(150) NOT NULL
  - `isbn` VARCHAR(13) UNIQUE NOT NULL
  - `genre` VARCHAR(50)
  - `published_year` INTEGER
  - `total_copies` INTEGER NOT NULL DEFAULT 1

  **`members`**
  - `id` SERIAL PRIMARY KEY
  - `full_name` VARCHAR(100) NOT NULL
  - `email` VARCHAR(150) UNIQUE NOT NULL
  - `joined_at` TIMESTAMPTZ DEFAULT NOW()
  - `is_active` BOOLEAN DEFAULT TRUE

  **`borrowings`**
  - `id` SERIAL PRIMARY KEY
  - `book_id` INTEGER NOT NULL REFERENCES `books(id)`
  - `member_id` INTEGER NOT NULL REFERENCES `members(id)`
  - `borrowed_at` TIMESTAMPTZ DEFAULT NOW()
  - `due_date` DATE NOT NULL
  - `returned_at` TIMESTAMPTZ (nullable — NULL means not yet returned)

- After creating all tables, run `\d borrowings` to show the foreign key constraints
- Think about: what would happen if you tried to insert a borrowing with a `book_id` that doesn't exist?

**Expected output**
```
library_db=# \dt
          List of relations
 Schema |    Name    | Type  |  Owner
--------+------------+-------+---------
 public | books      | table | devuser
 public | borrowings | table | devuser
 public | members    | table | devuser
```

**File:** `task_03.sql`

---

## Task 4 — Build the hospital schema

**Scenario**
A private hospital needs a database to replace their Excel files. The head doctor says: "We have doctors, patients, and appointments. Each appointment is between one patient and one doctor, has a scheduled time, a department, and notes."

**Your task**
- Create database `hospital_db`
- Create table `doctors`:
  - `id`, `full_name` (NOT NULL), `specialty` (NOT NULL), `phone` (UNIQUE), `email` (UNIQUE NOT NULL), `hired_at` (TIMESTAMPTZ DEFAULT NOW())
- Create table `patients`:
  - `id`, `full_name` (NOT NULL), `date_of_birth` (DATE NOT NULL), `blood_type` (VARCHAR(5)), `phone`, `registered_at` (TIMESTAMPTZ DEFAULT NOW())
- Create table `appointments`:
  - `id`, `patient_id` (FK → patients), `doctor_id` (FK → doctors), `scheduled_at` (TIMESTAMPTZ NOT NULL), `department` (VARCHAR(100) NOT NULL), `notes` (TEXT), `status` (VARCHAR(20) DEFAULT `'scheduled'`)
- Add a `CHECK` constraint on `appointments.status` so it only accepts: `'scheduled'`, `'completed'`, `'cancelled'`
- Verify with `\d appointments`

**Expected output**
```
hospital_db=# \d appointments
                     Table "public.appointments"
    Column      |            Type             | Nullable |    Default
----------------+-----------------------------+----------+---------------
 id             | integer                     | not null | nextval(...)
 patient_id     | integer                     | not null |
 doctor_id      | integer                     | not null |
 scheduled_at   | timestamp with time zone    | not null |
 department     | character varying(100)      | not null |
 notes          | text                        |          |
 status         | character varying(20)       |          | 'scheduled'
Check constraints:
    "appointments_status_check" CHECK (status IN ('scheduled','completed','cancelled'))
```

**File:** `task_04.sql`

---

## Task 5 — Insert and inspect real data

**Scenario**
Lola's coffee shop database from Task 2 is ready. Now it's opening day. Lola wants to add her 6 menu items and record the first 5 sales of the day — then verify everything looks correct.

**Your task**
- Connect to your `coffee_db` from Task 2
- Insert 6 menu items (mix of categories and prices, some unavailable):
  - Espresso — Hot Drinks — 12,000 — available
  - Cappuccino — Hot Drinks — 18,000 — available
  - Iced Latte — Cold Drinks — 22,000 — available
  - Green Tea — Hot Drinks — 10,000 — available
  - Cheesecake — Food — 35,000 — available
  - Seasonal Special — Cold Drinks — 25,000 — NOT available (sold out)
- Insert 5 sales records referencing the correct `item_id`s
- Run these queries and show the output:
  - `SELECT * FROM menu_items;`
  - `SELECT * FROM sales;`
  - `SELECT * FROM menu_items WHERE available = TRUE ORDER BY price;`
  - `SELECT * FROM menu_items WHERE available = FALSE;`

**Expected output**
```
coffee_db=# SELECT name, price, available FROM menu_items ORDER BY price;
      name       | price  | available
-----------------+--------+-----------
 Green Tea       |  10000 | t
 Espresso        |  12000 | t
 Cappuccino      |  18000 | t
 Iced Latte      |  22000 | t
 Seasonal Special|  25000 | f
 Cheesecake      |  35000 | t
(6 rows)
```

**File:** `task_05.sql`

