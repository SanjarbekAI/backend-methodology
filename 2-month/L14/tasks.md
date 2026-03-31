# L14 Tasks — Closures & Higher-Order Functions

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The configurable discount factory

**Scenario**
An e-commerce platform has different discount tiers for different customer categories: regular (5%), member (15%), and VIP (30%). Instead of writing three separate functions, the system uses a closure factory.

**Your task**
- Write `make_discount(percent)` that returns a closure `apply_discount(price)`
- Create three discount functions: `regular_discount`, `member_discount`, `vip_discount`
- Apply each to a list of 4 prices and print the results in a formatted table

**Expected output**
```
Price       Regular(5%)   Member(15%)   VIP(30%)
100,000      95,000        85,000        70,000
250,000     237,500       212,500       175,000
80,000       76,000        68,000        56,000
500,000     475,000       425,000       350,000
```

**File:** `task_01.py`

---

## Task 2 — The data pipeline

**Scenario**
A bank's data processing team receives a raw list of transaction amounts as strings (from a CSV export). They need to clean the data, filter out invalid entries, convert to numbers, and calculate the total using a functional pipeline.

**Your task**
- Start with: `raw_data = ["1500.50", "200", "INVALID", "850.75", "-100", "3200", "ERROR", "420.00"]`
- Step 1: Use `filter()` to keep only entries that are valid positive numbers (use `.replace(".", "").isdigit()` as a helper check, and also filter out negatives after conversion)
- Step 2: Use `map()` to convert valid strings to floats
- Step 3: Use `reduce()` to calculate the total
- Print each step's result and the final total

**Expected output**
```
Raw data:    ['1500.50', '200', 'INVALID', '850.75', '-100', '3200', 'ERROR', '420.00']
Valid str:   ['1500.50', '200', '850.75', '3200', '420.00']
As floats:   [1500.5, 200.0, 850.75, 3200.0, 420.0]
Total:       6171.25
```

**File:** `task_02.py`

---

## Task 3 — The grade filter and counter

**Scenario**
A university's academic reporting system processes a list of student records. It needs to filter students by various criteria using `filter()` and transform data using `map()`.

**Your task**
- Define 8 student dictionaries: `{"name": ..., "gpa": ..., "year": ...}`
- Use `filter()` to find students with GPA ≥ 3.5
- Use `filter()` to find year-4 students
- Use `map()` to generate a list of formatted strings: `"Name (GPA: X.X)"`
- Print each result group

**Expected output**
```
Honor students (GPA ≥ 3.5):
  Kamola Yusupova (GPA: 3.8)
  Sara Karimova (GPA: 3.9)
  Bobur Nazarov (GPA: 3.5)

Year 4 students:
  Rustam Toshmatov (GPA: 3.2)
  Nodira Hasanova (GPA: 2.9)

All students formatted:
  Kamola Yusupova (GPA: 3.8)
  ...
```

**File:** `task_03.py`

---

## Task 4 — The salary processor

**Scenario**
An HR tool processes payroll data. It uses closures to create configurable tax and bonus calculators, then applies them to all employee salaries.

**Your task**
- Write `make_tax_deductor(rate)` — closure that deducts a tax percentage
- Write `make_bonus_adder(percent)` — closure that adds a bonus percentage
- Define: `salaries = [3500000, 5200000, 7800000, 4100000, 6300000]`
- Apply 12% tax deduction using `map()`
- Apply 10% bonus using `map()`
- Find employees who earn above 5,000,000 before tax using `filter()`
- Print all three results

**Expected output**
```
After 12% tax:  [3,080,000 | 4,576,000 | 6,864,000 | 3,608,000 | 5,544,000]
After 10% bonus:[3,850,000 | 5,720,000 | 8,580,000 | 4,510,000 | 6,930,000]
High earners:   [5,200,000 | 7,800,000 | 6,300,000]
```

**File:** `task_04.py`

---

## Task 5 — The search factory

**Scenario**
A product search engine creates specialized search functions for different product categories. Each search function is pre-configured with the category using a closure, so the search logic is reusable.

**Your task**
- Write `make_category_search(category)` that returns `search(products)` — a closure that filters products by that category
- Define a list of 10 products: `{"name": ..., "category": ..., "price": ...}`
- Create three search functions: `search_electronics`, `search_clothing`, `search_books`
- Call each and print the results
- Combine `map()` to extract just the names from each search result

**Expected output**
```
Electronics:
  Laptop — 8,500,000 sum
  Headphones — 350,000 sum
  Webcam — 580,000 sum

Clothing:
  T-Shirt — 85,000 sum
  Jacket — 420,000 sum

Books:
  Python Crash Course — 95,000 sum
  Clean Code — 110,000 sum
```

**File:** `task_05.py`

