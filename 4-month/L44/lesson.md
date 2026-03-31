# L44 — Practice: Full Terminal App with PostgreSQL

## Project brief
You are building **StoreOS** — a complete command-line store management system for a small electronics retail business. This is your 4-month capstone project. It combines everything: PostgreSQL database design with constraints and indexes, Python with psycopg2 and the repository pattern, transactions for critical operations, Git with feature branches throughout development, and a polished terminal interface.

The business owner will use this system daily from her terminal to manage products, customers, orders, and generate business reports. It must be robust, fast, and professional.

---

## System overview

```
StoreOS/
├── .env                        ← credentials (not in Git)
├── .env.example                ← template (in Git)
├── .gitignore
├── requirements.txt
├── README.md
├── migrations/
│   ├── 001_create_schema.sql
│   └── 002_seed_data.sql
├── db/
│   ├── connection.py           ← get_connection() factory
│   └── repositories/
│       ├── product_repo.py
│       ├── customer_repo.py
│       ├── order_repo.py
│       └── report_repo.py
├── app/
│   ├── menu.py                 ← menu display functions
│   └── handlers.py             ← input handling, calls repositories
└── main.py                     ← entry point, main loop
```

---

## Database schema requirements

### Table: `products`
- `id` SERIAL PRIMARY KEY
- `name` VARCHAR(200) NOT NULL
- `category` VARCHAR(50) NOT NULL
- `sku` VARCHAR(50) UNIQUE NOT NULL
- `price` NUMERIC(12,2) NOT NULL CHECK (price > 0)
- `stock` INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0)
- `is_active` BOOLEAN DEFAULT TRUE
- `created_at` TIMESTAMPTZ DEFAULT NOW()
- Index on `category`, index on `sku`

### Table: `customers`
- `id` SERIAL PRIMARY KEY
- `full_name` VARCHAR(100) NOT NULL
- `email` VARCHAR(150) UNIQUE NOT NULL
- `phone` VARCHAR(20)
- `city` VARCHAR(50)
- `total_orders` INTEGER DEFAULT 0
- `total_spent` NUMERIC(14,2) DEFAULT 0
- `registered_at` TIMESTAMPTZ DEFAULT NOW()
- Index on `email`

### Table: `orders`
- `id` SERIAL PRIMARY KEY
- `customer_id` INTEGER NOT NULL REFERENCES `customers(id)` ON DELETE RESTRICT
- `status` VARCHAR(20) DEFAULT `'pending'` CHECK (status IN ('pending','processing','shipped','delivered','cancelled'))
- `total_amount` NUMERIC(14,2) NOT NULL CHECK (total_amount > 0)
- `created_at` TIMESTAMPTZ DEFAULT NOW()

### Table: `order_items`
- `id` SERIAL PRIMARY KEY
- `order_id` INTEGER NOT NULL REFERENCES `orders(id)` ON DELETE CASCADE
- `product_id` INTEGER NOT NULL REFERENCES `products(id)` ON DELETE RESTRICT
- `quantity` INTEGER NOT NULL CHECK (quantity > 0)
- `unit_price` NUMERIC(12,2) NOT NULL — snapshot of price at time of order
- UNIQUE(order_id, product_id)

### Views
- `order_summary` — order_id, customer name, email, item_count, total_amount, status, created_at
- `product_sales_report` — product_id, name, category, times_ordered, total_qty_sold, total_revenue

---

## Full requirements

### Product management
1. View all active products (formatted table with stock status using CASE WHEN)
2. Search products by name or category (ILIKE)
3. Add a new product (with UniqueViolation handling for duplicate SKU)
4. Update product price (with RETURNING confirmation)
5. Restock product (UPDATE stock, show before/after)
6. Deactivate a product (soft delete — sets is_active = FALSE)

### Customer management
7. View all customers (id, name, email, city, total_orders, total_spent)
8. Search customer by name or email
9. Register a new customer (with UniqueViolation handling for duplicate email)
10. View a customer's full order history with totals

### Order management (transactional)
11. Place a new order — ATOMIC transaction:
    - Validate all items have sufficient stock
    - INSERT into orders (RETURNING id)
    - INSERT each order_item with snapshot price
    - UPDATE stock for each product
    - UPDATE customer's total_orders and total_spent
    - COMMIT — or ROLLBACK everything on any failure
12. Update order status (pending → processing → shipped → delivered)
13. Cancel an order — ATOMIC: restore all stock, set status to cancelled
14. View order details (JOIN order_items + products + customer)

### Reports
15. Daily summary: total orders today, revenue today, pending orders, low stock count
16. Top 5 products by revenue this month (window function or GROUP BY)
17. Top 5 customers by total spent
18. Revenue by category (GROUP BY with % of total using window function)
19. Low stock alert: all products with stock <= 5

---

## Milestones

**Milestone 1 (0:00–0:30) — Database & connection layer**
- Write and run `001_create_schema.sql` — all 4 tables, constraints, indexes, views
- Write and run `002_seed_data.sql` — insert 10 products, 5 customers, 5 orders with items
- Build `db/connection.py` with `get_connection()` loading from `.env`
- Verify: connect from Python, run `SELECT COUNT(*) FROM products`, print the result
- Git: all on branch `feature/database-setup` → commit → PR (even if solo, practice the workflow) → merge

**Milestone 2 (0:30–1:00) — Repository layer**
- Build all 4 repository classes with all methods listed above
- Each repository is tested independently (temporary `if __name__ == "__main__":` block)
- Test: insert a product, search it, update its price, check it appears in the view
- Git: `feature/repository-layer` → merge

**Milestone 3 (1:00–1:30) — Application layer & order transactions**
- Build `app/menu.py` (pure display — no DB calls) and `app/handlers.py` (receives input, calls repos)
- Implement `main.py` menu loop — all 19 menu options respond correctly
- Focus: the `place_order` and `cancel_order` transactions — test rollback by intentionally failing mid-transaction
- Git: `feature/app-layer` → merge

**Milestone 4 (1:30–2:00) — Reports & polish**
- Implement all 5 report queries (items 15–19) with formatted output
- Add error handling throughout — no unhandled exceptions should crash the app
- Write `README.md` with setup steps and usage
- Final `git log --oneline --graph` review
- Demo: full workflow — add customer → place order with 3 items → update status → cancel it → check stock restored → run daily report

---

## Bonus challenges
1. Add a `NUMERIC(3,1)` `rating` column to products, and a `reviews` table (product_id, customer_id, rating, comment, created_at). Add a menu option to rate a purchased product and show the average rating per product.
2. Export any report to a `.csv` file using Python's `csv` module
3. Add a `search_orders` function that finds orders by customer name, product name, date range, or status — combining multiple optional filters dynamically in Python

