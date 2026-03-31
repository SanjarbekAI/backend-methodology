# L04 Tasks — Strings & Formatting

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The email parser

**Scenario**
A user registration system receives a raw email address and needs to extract the username (the part before `@`) and the domain (the part after `@`) separately. The system must also check that the email contains `@` and ends with `.com`.

**Your task**
- Define: `email = "rustam.nazarov@techcorp.com"`
- Use slicing or `split()` to extract the username and domain
- Check if the email contains `@` using `find()` or `in`
- Check if it ends with `.com` using `endswith()`
- Print all results clearly

**Expected output**
```
Full email:  rustam.nazarov@techcorp.com
Username:    rustam.nazarov
Domain:      techcorp.com
Has @:       True
Ends .com:   True
```

**File:** `task_01.py`

---

## Task 2 — The name formatter

**Scenario**
A government database received citizen records from multiple sources, and the names are stored inconsistently — some are all caps, some are all lowercase, and many have extra spaces. A cleanup script must standardize every name to Title Case with no extra whitespace.

**Your task**
- Define a list of 5 messy names (as separate variables — lists come in a later lesson):
  ```python
  name1 = "  LAYLA YUSUPOVA  "
  name2 = "kamol toshmatov"
  name3 = "SARA   karimova"
  name4 = "   nodira HASANOVA"
  name5 = "BOBUR nazarov  "
  ```
- For each name: strip whitespace, then apply `.title()`
- Print original and cleaned version side by side

**Expected output**
```
"  LAYLA YUSUPOVA  "   →   "Layla Yusupova"
"kamol toshmatov"      →   "Kamol Toshmatov"
"SARA   karimova"      →   "Sara   Karimova"
"   nodira HASANOVA"   →   "Nodira Hasanova"
"BOBUR nazarov  "      →   "Bobur Nazarov"
```

**File:** `task_02.py`

---

## Task 3 — The product label generator

**Scenario**
A warehouse management system prints labels for packages. Each label must show the product name (padded to fit exactly 20 characters), the SKU code (uppercase), the price formatted to 2 decimal places, and a separator line.

**Your task**
- Define: `product_name = "wireless headphones"`, `sku = "ab-2047"`, `price = 49.9`
- Format the product name: capitalize it properly
- Format the SKU: convert to uppercase
- Format the price: show exactly 2 decimal places using an f-string
- Print a label that looks clean and aligned (use f-string padding)

**Expected output**
```
==============================
Product:  Wireless Headphones
SKU:      AB-2047
Price:    49.90 USD
==============================
```

**File:** `task_03.py`

---

## Task 4 — The password validator

**Scenario**
A security system checks whether a new password meets the company's rules before accepting it. The check is done by analyzing the string itself — no loops yet, just string methods.

**Your task**
- Define: `password = "MyPass2024!"`
- Check and print:
  - Length is at least 8 characters: `len(password) >= 8`
  - Does not start with a number: use `password[0].isdigit()` → should be False
  - Contains uppercase letters: `password != password.lower()`
  - Contains digits: use `any(c.isdigit() for c in password)` ← you can use this line as-is
  - Replace all digits with `*` and print the masked version

**Expected output**
```
Password:      MyPass2024!
Length OK:     True
Starts digit:  False
Has uppercase: True
Has digit:     True
Masked:        MyPass****!
```

**File:** `task_04.py`

---

## Task 5 — The report card formatter

**Scenario**
A school system generates formatted student report cards. Each card must display the student's name, subject scores, and a summary — all nicely aligned using f-string formatting.

**Your task**
- Define: student name, and scores for 4 subjects (as floats)
- Calculate the average score
- Print the report card with:
  - Student name in the header (centered in a 30-char field using f-string formatting)
  - Each subject and score, score formatted to 1 decimal place
  - Average at the bottom, formatted to 2 decimal places
  - Pass/Fail status based on average ≥ 60

**Expected output**
```
==============================
       Kamola Yusupova        
==============================
Math:         87.5
Science:      74.0
English:      91.0
History:      68.0
------------------------------
Average:      80.12
Status:       PASS
==============================
```

**File:** `task_05.py`

---

## Task 6 — The message template engine

**Scenario**
A marketing team sends personalized SMS messages to customers. They have a template with placeholders that must be filled in with customer data to generate the final message.

**Your task**
- Define a multi-line template string with `{}` placeholders:
  ```
  Dear {name},
  Your order #{order_id} has been confirmed.
  Total: {total} USD
  Expected delivery: {delivery_date}
  Thank you for choosing {company}!
  ```
- Fill in the template using an f-string (define all 5 variables first)
- Print the final message
- Also print the character count of the final message using `len()`

**Expected output**
```
Dear Rustam,
Your order #10847 has been confirmed.
Total: 129.99 USD
Expected delivery: April 3, 2026
Thank you for choosing TechStore!

Message length: 132 characters
```
*(Exact length will depend on your values.)*

**File:** `task_06.py`

