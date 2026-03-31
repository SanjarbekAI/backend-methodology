# L12 Tasks — Functions: Basics & Scope

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The tax calculator

**Scenario**
A small business owner's accounting tool calculates the VAT (value-added tax) and final price for any product. The calculation must be reusable for any price and any tax rate.

**Your task**
- Write a function `calculate_vat(price, tax_rate)` that returns the tax amount
- Write a function `final_price(price, tax_rate)` that returns price + tax
- Call both functions for 3 different products and print a formatted receipt for each

**Expected output**
```
Product: Laptop
Base price:  8,500,000 sum
VAT (12%):   1,020,000 sum
Final price: 9,520,000 sum

Product: Mouse
Base price:  120,000 sum
VAT (12%):    14,400 sum
Final price:  134,400 sum
```

**File:** `task_01.py`

---

## Task 2 — The BMI checker

**Scenario**
A hospital's patient intake system calculates BMI (Body Mass Index) for each patient and classifies them according to WHO standards. The nurse enters weight and height, and the system prints the result.

**Your task**
- Write `calculate_bmi(weight_kg, height_m)` — returns the BMI rounded to 1 decimal
- Write `classify_bmi(bmi)` — returns the category string:
  - Under 18.5 → "Underweight"
  - 18.5–24.9 → "Normal weight"
  - 25–29.9 → "Overweight"
  - 30+ → "Obese"
- Call both for 3 different patients and print results

**Expected output**
```
Patient: Rustam | Weight: 78 kg | Height: 1.75 m
BMI: 25.5 — Overweight

Patient: Layla | Weight: 55 kg | Height: 1.65 m
BMI: 20.2 — Normal weight
```

**File:** `task_02.py`

---

## Task 3 — The password strength tester

**Scenario**
A user registration system evaluates password strength before accepting it. The evaluation is done by a function that checks multiple criteria and returns a score and label.

**Your task**
- Write `check_password_strength(password)` that:
  - Returns `(score, label)` where score is 0–4 and label is one of: Weak / Fair / Good / Strong
  - +1 point: length ≥ 8
  - +1 point: has uppercase letter
  - +1 point: has a digit
  - +1 point: has a special character (check for any of `!@#$%^&*`)
- Test with at least 4 different passwords and print the score and label for each

**Expected output**
```
"abc"         → Score: 0/4 — Weak
"hello123"    → Score: 2/4 — Fair
"Hello123"    → Score: 3/4 — Good
"Hello123!"   → Score: 4/4 — Strong
```

**File:** `task_03.py`

---

## Task 4 — The invoice generator

**Scenario**
A freelance developer's billing tool generates formatted invoices. Each invoice is produced by a function that takes project details and returns a formatted multi-line string ready to print or save.

**Your task**
- Write `generate_invoice(client, project, hours, rate, tax_rate)` that:
  - Calculates subtotal, tax, and total
  - Returns a formatted multi-line invoice string
- Call the function for 2 different clients
- Print the returned invoice string for each

**Expected output**
```
========================================
             INVOICE
========================================
Client:    TechStartup Ltd
Project:   Backend API Development
Hours:     40
Rate:      150,000 sum/hr
----------------------------------------
Subtotal:  6,000,000 sum
Tax (12%):   720,000 sum
TOTAL:     6,720,000 sum
========================================
```

**File:** `task_04.py`

---

## Task 5 — The search function

**Scenario**
A library management system needs a function to search for a book by title. The function looks through a list of book dictionaries and returns the matching book or `None` if not found.

**Your task**
- Define a list of 6 book dictionaries: `{"title": "...", "author": "...", "year": ...}`
- Write `find_book(title, library)` that:
  - Searches case-insensitively (convert both to `.lower()` before comparing)
  - Returns the book dictionary if found, or `None` if not
- Call it with 3 searches: 2 that exist and 1 that doesn't
- Use `if result is None` to handle the not-found case

**Expected output**
```
Search: "the great gatsby"
Found: The Great Gatsby by F. Scott Fitzgerald (1925)

Search: "1984"
Found: 1984 by George Orwell (1949)

Search: "invisible man"
Not found in the library.
```

**File:** `task_05.py`

