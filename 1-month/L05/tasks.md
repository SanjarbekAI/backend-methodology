# L05 Tasks — Booleans & if...else

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The age gate

**Scenario**
A cinema ticketing system needs to classify customers by age and assign the correct ticket type: Child (under 12), Teen (12–17), Adult (18–64), or Senior (65 and above). The system also applies a discount flag for children and seniors.

**Your task**
- Define: `age = 14`
- Use `if/elif/else` to determine and print the ticket category
- Print whether a discount applies (True for Child and Senior, False otherwise)
- Test your code with at least 3 different age values using comments to show expected output

**Expected output** (for age = 14)
```
Age: 14
Category: Teen
Discount: False
```

**File:** `task_01.py`

---

## Task 2 — The grade classifier

**Scenario**
A university's academic system needs to convert a numeric score into a letter grade and a GPA point value. The registrar's office will use this for official transcripts.

**Your task**
- Define: `score = 83`
- Use `if/elif/else` to classify:
  - 90–100 → A, 4.0 GPA
  - 80–89  → B, 3.0 GPA
  - 70–79  → C, 2.0 GPA
  - 60–69  → D, 1.0 GPA
  - Below 60 → F, 0.0 GPA
- Also determine pass/fail status (F = fail)
- Print score, letter grade, GPA, and status

**Expected output** (for score = 83)
```
Score:  83
Grade:  B
GPA:    3.0
Status: Pass
```

**File:** `task_02.py`

---

## Task 3 — The shipping calculator

**Scenario**
An e-commerce platform calculates shipping costs based on delivery zone and order weight. Members always get free shipping on orders above 50 USD, regardless of zone.

**Your task**
- Define: `zone = "international"`, `weight_kg = 2.5`, `order_total = 45.0`, `is_member = False`
- Shipping rules:
  - If member AND order_total >= 50 → free shipping
  - Zone "local" → 5000 sum base + 2000 per kg
  - Zone "national" → 15000 sum base + 5000 per kg
  - Zone "international" → 50000 sum base + 12000 per kg
- Print the shipping cost and whether it was free

**Expected output** (for the values above)
```
Zone:          international
Weight:        2.5 kg
Order total:   45.0 USD
Member:        False
Shipping cost: 80000 sum
Free shipping: False
```

**File:** `task_03.py`

---

## Task 4 — The ATM access system

**Scenario**
An ATM system checks multiple conditions before allowing a transaction. It must verify the card is active, the PIN is correct, and the withdrawal amount does not exceed the account balance or the daily limit.

**Your task**
- Define: `card_active = True`, `pin_entered = 4521`, `correct_pin = 4521`, `balance = 1500000`, `withdrawal = 200000`, `daily_limit = 500000`
- Use nested conditions to determine:
  - If card is not active → "Card blocked. Contact your bank."
  - If PIN is wrong → "Incorrect PIN. 2 attempts remaining."
  - If withdrawal > balance → "Insufficient funds."
  - If withdrawal > daily_limit → "Exceeds daily limit."
  - Otherwise → "Transaction approved. Dispensing cash."
- Print only the appropriate message

**Expected output** (for values above)
```
Transaction approved. Dispensing cash.
```

**File:** `task_04.py`

---

## Task 5 — The status code responder

**Scenario**
A web API logging tool needs to read an HTTP status code and print a human-readable description of what it means. The tool uses Python's `match` statement for clean, readable code.

**Your task**
- Define: `status_code = 403`
- Use a `match` statement to handle:
  - 200 → "OK — Request successful"
  - 201 → "Created — Resource added successfully"
  - 400 → "Bad Request — Invalid input from client"
  - 401 → "Unauthorized — Authentication required"
  - 403 → "Forbidden — You do not have permission"
  - 404 → "Not Found — Resource does not exist"
  - 500 → "Internal Server Error — Something went wrong"
  - Default → "Unknown status code"
- Print the status code and its description

**Expected output** (for status_code = 403)
```
Status 403: Forbidden — You do not have permission
```

**File:** `task_05.py`

---

## Task 6 — The loan eligibility checker

**Scenario**
A bank's loan processing system checks whether an applicant is eligible for a personal loan based on income, credit score, existing debt, and employment status. It must explain the decision clearly.

**Your task**
- Define: `monthly_income = 3500000`, `credit_score = 720`, `has_existing_debt = False`, `is_employed = True`, `loan_amount = 50000000`
- Eligibility rules:
  - Must be employed
  - Credit score must be ≥ 650
  - No existing debt
  - Loan amount must be ≤ 12 months of income
- If all conditions pass → "Loan approved"
- If any condition fails → "Loan denied" and print which condition(s) failed
- Use individual booleans for each check and combine them at the end

**Expected output** (for values above)
```
Employment:    OK
Credit score:  OK
Existing debt: OK
Loan ratio:    OK

Result: Loan approved ✓
```

**File:** `task_06.py`

