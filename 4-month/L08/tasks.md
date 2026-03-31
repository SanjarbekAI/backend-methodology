# L41 Tasks — PostgreSQL + Python (psycopg2)

Complete the tasks below. Create a `.py` file for each task. Store credentials in a `.env` file — never hardcode them.

---

## Task 1 — First connection — the database ping tool

**Scenario**
Every time Jasur starts work on a project, his first step is running a "database health check" script: can we connect? Which database is it? How many rows are in the main tables? This gives him confidence before writing a single line of business logic.

**Your task**
- Create a `.env` file with your DB credentials (not committed to Git)
- Install `psycopg2-binary` and `python-dotenv`
- Write `task_01.py` that:
  - Loads credentials from `.env` using `load_dotenv()`
  - Connects to any database you created in previous lessons (e.g., `shop_db`)
  - Prints the PostgreSQL server version: `SELECT version()`
  - Lists all tables in the current schema:
    ```sql
    SELECT tablename FROM pg_tables WHERE schemaname = 'public' ORDER BY tablename
    ```
  - For each table, prints its row count: `SELECT COUNT(*) FROM {table_name}`
  - Handles `OperationalError` gracefully (wrong password, DB offline) with a clear message
  - Uses context managers (`with`) for both connection and cursor

**Expected output**
```
✓ Connected to PostgreSQL
Server version: PostgreSQL 15.3 on x86_64-pc-linux-gnu

Tables in 'shop_db':
  customers     →  12 rows
  order_items   →  28 rows
  orders        →  15 rows
  products      →  20 rows

Connection closed.
```

**File:** `task_01.py`

---

## Task 2 — Product manager CLI — full CRUD from the terminal

**Scenario**
The warehouse manager at a small electronics store has no web interface — she manages the product catalog entirely through a terminal script you built her. She needs to: view all products, search by name, add new products, update prices, and deactivate products that are discontinued.

**Your task**
- Use (or create) a `products` table in PostgreSQL with: id, name, category, price, stock, is_active, created_at
- Write `task_02.py` — a terminal menu app:
  ```
  === Product Manager ===
  1. View all active products
  2. Search product by name
  3. Add new product
  4. Update product price
  5. Deactivate product
  6. Exit
  ```
- Each menu option calls a dedicated function (e.g., `view_products(conn)`, `search_product(conn)`)
- All SQL uses parameterized queries with `%s` — never f-strings for SQL
- Use `RealDictCursor` so data is accessible by column name
- After any INSERT/UPDATE: print the affected row using `RETURNING`
- Handle `UniqueViolation`, `NotNullViolation`, and general `DatabaseError` with friendly messages
- The app loops until the user selects "Exit"

**Expected output**
```
=== Product Manager ===
Choice: 3
Name: Xiaomi Redmi Note 13
Category: Phone
Price: 2850000
Stock: 25

✓ Product added!
  ID: 21 | Xiaomi Redmi Note 13 | 2,850,000 sum | Stock: 25

Choice: 4
Product ID to update: 21
New price: 2750000

✓ Price updated!
  Xiaomi Redmi Note 13: 2,850,000 → 2,750,000 sum
```

**File:** `task_02.py`

---

## Task 3 — Customer search tool — parameterized queries

**Scenario**
A call center operator at a telecom company types a customer's name or phone number into a search field. Your Python script must find all matching customers, show their recent orders, and display the total amount they've spent — all from the terminal, in under a second.

**Your task**
- Use (or create) `customers` and `orders` tables
- Write `task_03.py` with these search functions:
  1. `search_by_name(conn, query: str)` — uses `ILIKE '%query%'` to find matching customers
  2. `search_by_phone(conn, phone: str)` — exact match on phone
  3. `get_customer_orders(conn, customer_id: int)` — returns all orders for that customer, newest first
  4. `get_customer_summary(conn, customer_id: int)` — returns: total orders, total spent, avg order, last order date
- Main loop: user enters a search term, results are displayed, user can select a customer by ID to see their full history
- All queries use `%s` parameterized placeholders — no string concatenation for SQL
- Use `RealDictCursor` throughout

**Expected output**
```
Search customer (name or leave blank to search by phone): Nilufar

Results:
  ID: 1 | Nilufar Karimova | nilufar@mail.com | Tashkent
  ID: 7 | Nilufar Tosheva  | n.tosh@mail.com  | Samarkand

Enter customer ID for full details (or 0 to search again): 1

=== Customer: Nilufar Karimova ===
Summary: 5 orders | Total: 12,450,000 sum | Avg: 2,490,000 | Last: 2025-01-10

Orders:
  #24 | iPhone 15     | 8,200,000 | completed | 2025-01-10
  #18 | AirPods Pro   | 1,450,000 | completed | 2024-12-22
  ...
```

**File:** `task_03.py`

---

## Task 4 — Repository pattern — a clean database layer

**Scenario**
Dilnoza is refactoring a messy script where SQL queries are scattered across 600 lines of code. Her tech lead says: "We need a proper repository layer — each table gets its own class with clean methods. The rest of the app should never write SQL directly." Dilnoza needs to build this from scratch.

**Your task**
- Create a `library_db` database with `books`, `members`, and `borrowings` tables (from L36 Task 3, or recreate)
- Write `task_04.py` with these repository classes:

  **`BookRepository`**
  - `get_all() → list[dict]`
  - `get_by_id(id) → dict | None`
  - `search(query: str) → list[dict]` — searches title and author with ILIKE
  - `create(title, author, isbn, genre, year, copies) → int` (returns new id)
  - `update_copies(id, new_count) → bool`

  **`MemberRepository`**
  - `get_all(active_only=True) → list[dict]`
  - `get_by_email(email) → dict | None`
  - `create(full_name, email) → int`
  - `deactivate(id) → bool`

  **`BorrowingRepository`**
  - `borrow(book_id, member_id, due_date) → int`
  - `return_book(borrowing_id) → bool` — sets `returned_at = NOW()`
  - `get_active_borrowings() → list[dict]` — all not yet returned, with book title and member name (JOIN)
  - `get_overdue() → list[dict]` — due_date < TODAY and returned_at IS NULL

- Write a `main()` demo that exercises all repository methods with real data

**Expected output**
```
=== Active Borrowings ===
  Borrowing #3 | "Clean Code" | Member: Sardor Toshev | Due: 2025-01-20
  Borrowing #5 | "Python Crash Course" | Member: Malika | Due: 2025-01-25

=== Overdue Books ===
  Borrowing #1 | "The Pragmatic Programmer" | Aziz Karimov | Was due: 2025-01-10
```

**File:** `task_04.py`

---

## Task 5 — Terminal app — inventory manager with error handling

**Scenario**
The operations manager at a pharmacy needs a terminal tool to manage daily inventory operations: receive new stock deliveries, process sales (reduce stock), view low-stock alerts, and generate a daily summary report — all backed by PostgreSQL, all running in the terminal.

**Your task**
- Create `pharmacy_db` with: `medicines` (id, name, category, stock_units, unit_price, reorder_level) and `transactions` (id, medicine_id, type: 'restock'|'sale', quantity, performed_by, created_at)
- Write `task_05.py` — a full terminal inventory manager:
  ```
  === Pharmacy Inventory ===
  1. View all medicines (stock status)
  2. Record a restock delivery
  3. Record a sale
  4. Low stock alert (below reorder level)
  5. Daily transaction report
  6. Exit
  ```
- Each operation:
  - **Restock:** `UPDATE medicines SET stock_units = stock_units + %s WHERE id = %s` + insert into transactions
  - **Sale:** Check if enough stock FIRST (Python logic), then subtract, then record transaction — if insufficient, print an error and don't update
  - **Low stock:** `WHERE stock_units <= reorder_level ORDER BY stock_units`
  - **Daily report:** SELECT from transactions + medicines JOIN, for today's date only
- Wrap all multi-step operations in a `try/except` with `conn.rollback()` on failure
- Use `RETURNING` to confirm every UPDATE/INSERT

**Expected output**
```
Choice: 3 (Record a sale)
Medicine ID: 5
Quantity sold: 50
Cashier name: Aziza

✓ Sale recorded!
  Paracetamol 500mg | -50 units | Remaining: 12 units
  ⚠ Warning: Stock is below reorder level (20)!

Choice: 4 (Low stock alert)
=== LOW STOCK ALERT ===
  Paracetamol 500mg  |  12 units  | Reorder level: 20  ← CRITICAL
  Ibuprofen 200mg    |  18 units  | Reorder level: 25  ← LOW
```

**File:** `task_05.py`

