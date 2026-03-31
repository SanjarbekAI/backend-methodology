# L16 Tasks — Comprehensions & Functional Style

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The price transformer

**Scenario**
An e-commerce platform needs to apply a seasonal sale: all items over 500,000 sum get a 20% discount, items under 500,000 get a 10% discount. The pricing team needs the new price list in a single clean operation.

**Your task**
- Define: `prices = [120000, 850000, 350000, 1200000, 75000, 620000, 290000]`
- Use a list comprehension with a ternary to apply the correct discount to each price
- Round each result to the nearest 1000 (use `round(x, -3)`)
- Print original prices and discounted prices side by side

**Expected output**
```
Original → Discounted
 120,000 →  108,000
 850,000 →  680,000
 350,000 →  315,000
1,200,000 → 960,000
  75,000 →   68,000
 620,000 →  496,000
 290,000 →  261,000
```

**File:** `task_01.py`

---

## Task 2 — The inventory filter

**Scenario**
A warehouse system needs to quickly find products that are low in stock, out of stock, or available. The operations team runs these queries multiple times a day on large product lists.

**Your task**
- Define a list of 8 product dicts: `{"name": ..., "stock": ..., "price": ...}`
- Use list comprehensions to create three filtered lists:
  - `out_of_stock`: stock == 0
  - `low_stock`: stock between 1 and 10 inclusive
  - `available`: stock > 10
- Print each list as formatted output

**Expected output**
```
Out of stock:
  - Wireless Earbuds
  - USB Hub

Low stock (1-10):
  - Keyboard (5 left)
  - HDMI Cable (3 left)

Available:
  - Laptop (42 units)
  - Mouse (28 units)
  - Monitor (15 units)
  - Webcam (11 units)
```

**File:** `task_02.py`

---

## Task 3 — The student grade tagger

**Scenario**
A university's grading system processes all student scores and produces a summary dictionary mapping each student's name to their letter grade and pass/fail status in one step.

**Your task**
- Define a list of student dicts: `{"name": ..., "score": ...}` (at least 7 students)
- Use a **dict comprehension** to create `grade_map` where:
  - Key = student name
  - Value = letter grade string: A (90+), B (80+), C (70+), D (60+), F (below 60)
- Use a **list comprehension** to get names of all students who failed
- Use a **set comprehension** to get all unique grades assigned

**Expected output**
```
Grade map:
  Kamola: B
  Rustam: A
  Sara: C
  Bobur: F
  Layla: B
  Nodira: D
  Ali: A

Failed students: ['Bobur']
Grades used: {'A', 'B', 'C', 'D', 'F'}
```

**File:** `task_03.py`

---

## Task 4 — The email domain analyzer

**Scenario**
A company's IT security team audits the email addresses of all registered users. They need to identify which email providers are being used, flag personal emails (non-company domain), and count users per domain.

**Your task**
- Define a list of 10 email addresses (mix of gmail, company, yahoo, etc.)
- Use a **set comprehension** to get all unique domains
- Use a **dict comprehension** to count how many users per domain
- Use a **list comprehension** to get all non-company emails (not ending in `@techcorp.com`)
- Print all three results

**Expected output**
```
Unique domains: {'gmail.com', 'techcorp.com', 'yahoo.com', 'mail.ru'}

Users per domain:
  techcorp.com: 4
  gmail.com:    3
  yahoo.com:    2
  mail.ru:      1

Personal emails (non-company):
  ali@gmail.com
  sara@yahoo.com
  ...
```

**File:** `task_04.py`

---

## Task 5 — The sales summary builder

**Scenario**
A retail analytics tool processes a list of daily sales transactions and builds a summary dictionary using comprehensions. The summary maps each product to its total revenue.

**Your task**
- Define a list of 10+ transaction dicts: `{"product": ..., "qty": ..., "unit_price": ...}`
- Use a **list comprehension** to compute the total value of each transaction (`qty * unit_price`)
- Use a **generator expression** inside `sum()` to calculate overall total revenue
- Use a **dict comprehension** to build `revenue_by_product`: product → total revenue
  (Hint: use `set()` to get unique products, then filter per product inside the comprehension)
- Print the transaction totals, overall total, and the revenue by product

**Expected output**
```
Transaction totals:
  Laptop x2:      17,000,000
  Mouse x5:          600,000
  ...

Total revenue: 23,450,000 sum

Revenue by product:
  Laptop:    17,000,000 sum
  Mouse:      1,200,000 sum
  Keyboard:   2,100,000 sum
  ...
```

**File:** `task_05.py`

