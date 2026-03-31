# L13 Tasks — Functions: Advanced

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The flexible order totaler

**Scenario**
A wholesale supplier's ordering system needs to calculate totals for orders that can contain any number of items. Each item has a price, and the function should also accept an optional discount percentage.

**Your task**
- Write `calculate_order(*prices, discount=0)` that:
  - Accepts any number of prices
  - Applies an optional discount (default 0%)
  - Returns `(subtotal, discount_amount, total)`
- Call it with 3 different order sizes (2 items, 5 items, 1 item)
- One call should apply a 15% discount

**Expected output**
```
Order 1: 2 items
Subtotal: 350,000 | Discount: 0 | Total: 350,000 sum

Order 2: 5 items — 15% off
Subtotal: 1,200,000 | Discount: 180,000 | Total: 1,020,000 sum
```

**File:** `task_01.py`

---

## Task 2 — The configurable report printer

**Scenario**
A data analytics tool generates formatted reports. The report function must be highly flexible — accepting any key-value data pairs as keyword arguments, plus optional display settings.

**Your task**
- Write `print_report(title, **data)` that:
  - Prints a bordered section with the title
  - Prints each key-value pair from `**data` on its own line
- Write `print_report_styled(title, width=40, border="=", **data)` that:
  - Uses `width` and `border` character for formatting
  - Prints each key-value pair
- Call both with realistic data (e.g., a sales report, a system status report)

**Expected output**
```
========================================
           Monthly Sales Report         
========================================
Region:    Central
Total:     8,500,000 sum
Orders:    142
Returns:   7

- - - - - - - - - - - - - - - - - - - -
         System Status Report           
- - - - - - - - - - - - - - - - - - - -
CPU:       23%
Memory:    61%
Uptime:    14 days
```

**File:** `task_02.py`

---

## Task 3 — The product sorter

**Scenario**
An e-commerce platform allows customers to sort their search results by different criteria: price (lowest first), name (A–Z), or rating (highest first). The sorting uses lambda functions as keys.

**Your task**
- Define a list of 5 product dictionaries: `{"name": ..., "price": ..., "rating": ...}`
- Write `sort_products(products, sort_by)` where `sort_by` can be `"price"`, `"name"`, or `"rating"`
- Inside the function, use lambda with `sorted()` for each sort type (rating: reverse=True)
- Call the function for all 3 sort types and print the results

**Expected output**
```
Sorted by price (low to high):
  Earbuds       — 89,000 sum — ⭐ 4.2
  Phone Stand   — 120,000 sum — ⭐ 3.8
  ...

Sorted by name (A–Z):
  ...

Sorted by rating (high to low):
  ...
```

**File:** `task_03.py`

---

## Task 4 — The smart greeting system

**Scenario**
A customer service platform sends personalized greetings. The greeting function has smart defaults (formal greeting, no title) but can be customized for VIP clients or specific occasions.

**Your task**
- Write `greet_customer(name, title="", greeting="Hello", sign_off="Best regards", **extra)`:
  - Constructs a personalized message using the parameters
  - If `title` is not empty, prepends it to the name
  - If any `**extra` keys are provided (e.g., `promo_code`, `loyalty_tier`), add them to the message
- Call it 4 times: basic, with title, with extra info, fully customized

**Expected output**
```
Hello, Rustam!
Best regards, Support Team

Hello, Dr. Karimova!
Best regards, Support Team

Hello, Sara!
Loyalty tier: Gold | Promo code: SAVE20
Best regards, Support Team
```

**File:** `task_04.py`

---

## Task 5 — The event logger

**Scenario**
A server monitoring system logs events. The logger function uses `*args` to accept multiple messages in one call, and `**kwargs` for metadata like severity level and source.

**Your task**
- Write `log_event(*messages, level="INFO", source="system")`:
  - Prints each message with the level and source prefix
  - If `level` is `"ERROR"`, also print a separator line after all messages
- Import `datetime` and include a timestamp
- Call it with: single message, multiple messages, error level

**Expected output**
```
[2026-03-30 09:15:22] [INFO] [system] Server started.

[2026-03-30 09:15:23] [INFO] [auth] User login: Rustam
[2026-03-30 09:15:23] [INFO] [auth] Session created: abc123

[2026-03-30 09:15:30] [ERROR] [database] Connection timeout.
[2026-03-30 09:15:30] [ERROR] [database] Retry attempt 1 failed.
============================================================
```

**File:** `task_05.py`

