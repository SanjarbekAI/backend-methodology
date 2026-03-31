# L44 Tasks — Practice: Full Terminal App with PostgreSQL

Complete both tasks below. This is your 4-month capstone. Submit a GitHub repository link.

---

## Task 1 — StoreOS: Core system

**Scenario**
Dilnora runs a small electronics store in Tashkent. She currently tracks everything in three separate Excel files and spends two hours every Monday manually counting stock and calculating revenue. She has asked you to build her a terminal-based management system. It must be reliable — she cannot afford data errors.

**Your task**
Build the complete StoreOS system as described in `lesson.md`. At minimum, your submission must include:

**Database layer** (verified running in PostgreSQL):
- All 4 tables created with proper constraints, foreign keys, and indexes
- Both views (`order_summary`, `product_sales_report`) created
- Seed data: 10 products in 3 categories, 5 customers, 8 orders with items
- Migration files committed: `migrations/001_create_schema.sql`, `migrations/002_seed_data.sql`

**Python layer** (all using psycopg2, parameterized queries, RealDictCursor):
- `db/connection.py` — `get_connection()` with `.env` support
- `ProductRepository` — all 6 product operations
- `CustomerRepository` — all 4 customer operations
- `OrderRepository` — `place_order()` and `cancel_order()` as full transactions, plus `update_status()` and `get_details()`
- `ReportRepository` — all 5 report queries

**Terminal interface:**
- `main.py` — working menu loop with all 19 options
- No unhandled exceptions — every error shows a user-friendly message
- All financial amounts formatted with thousands separators: `f"{amount:,.0f} sum"`

**Git requirements:**
- Minimum 10 commits with meaningful messages
- At least 3 feature branches visible in `git log --graph`
- `README.md` with setup instructions

**Expected output** (place_order demo)
```
=== Place New Order ===
Customer ID: 2
Add product (SKU or 0 to finish): ELEC-001
Quantity: 2
Add product (SKU or 0 to finish): PHON-003
Quantity: 1
Add product (SKU or 0 to finish): 0

--- Order Preview ---
  Wireless Keyboard x2   =  240,000 sum
  Samsung Galaxy A54 x1  = 2,850,000 sum
  ─────────────────────────────────────
  Total: 3,090,000 sum

Confirm? (y/n): y

✓ Order #9 placed successfully!
  Customer: Dilnora Yusupova | Total: 3,090,000 sum | Status: pending
```

**File:** Submit as a GitHub repository link

---

## Task 2 — StoreOS: Business reports demo

**Scenario**
It's the end of the month. Dilnora sits down with her terminal and runs the reports that tell her how the business performed. Your reporting module must answer all her questions accurately — pulled live from the PostgreSQL database in under a second.

**Your task**
Implement and demonstrate all 5 report types. Each report must be formatted cleanly for a non-technical user. Run all reports on your seeded data and show the output.

**Report 1 — Daily summary**
```
=== Daily Summary — 31 March 2025 ===
  Orders today:        4
  Revenue today:       8,450,000 sum
  Pending orders:      2
  Products low stock:  3 (≤5 units)
```

**Report 2 — Top 5 products by revenue this month**
```
=== Top Products (March 2025) ===
  #1  iPhone 15 Pro       | Electronics |  3 orders | 24,600,000 sum
  #2  Samsung Galaxy A54  | Phones      |  5 orders |  14,250,000 sum
  #3  AirPods Pro         | Accessories |  7 orders |  10,150,000 sum
  ...
```

**Report 3 — Top 5 customers by total spent**
```
=== Top Customers (All Time) ===
  #1  Sardor Toshmatov  | 8 orders | 18,500,000 sum
  #2  Nilufar Karimova  | 5 orders | 12,300,000 sum
  ...
```

**Report 4 — Revenue by category**
```
=== Revenue by Category (March 2025) ===
  Electronics   | 35,200,000 sum |  52.3%
  Phones        | 21,400,000 sum |  31.8%
  Accessories   |  10,700,000 sum |  15.9%
  ─────────────────────────────────────
  Total:          67,300,000 sum | 100.0%
```

**Report 5 — Low stock alert**
```
=== ⚠ LOW STOCK ALERT ===
  iPhone 15 Pro      | ELEC-001 |  2 units remaining
  USB-C Hub          | ELEC-007 |  4 units remaining
  Screen Protector   | ACCS-003 |  1 unit remaining
```

All 5 reports must be accessible from the main menu (option 15–19). The SQL behind each report must use the techniques from L37–L42 (GROUP BY, HAVING, window functions, CTEs where appropriate).

**File:** Part of the same GitHub repository as Task 1 (`report_repo.py` + menu integration)

