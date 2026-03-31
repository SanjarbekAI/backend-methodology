# L03 Tasks — Numbers, Casting & Operators

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The invoice calculator

**Scenario**
A small IT services company issues invoices to clients at the end of each project. A developer needs to write a script that calculates the final invoice amount including hours worked, hourly rate, and tax.

**Your task**
- Define: `hours_worked = 47`, `hourly_rate = 85000`, `tax_rate = 0.12`
- Calculate: subtotal (hours × rate), tax amount (subtotal × tax_rate), total (subtotal + tax)
- Print each value on a separate labelled line, formatted clearly

**Expected output**
```
Hours worked:  47
Hourly rate:   85000 sum
Subtotal:      3995000 sum
Tax (12%):     479400.0 sum
Total:         4474400.0 sum
```

**File:** `task_01.py`

---

## Task 2 — The grade checker

**Scenario**
A university's grading system needs to compare a student's score against the passing threshold and display whether they passed or failed each comparison check.

**Your task**
- Define: `student_score = 67`, `passing_score = 60`, `distinction_score = 85`
- Print the result of each comparison:
  - Did the student pass? (`student_score >= passing_score`)
  - Did the student get a distinction? (`student_score >= distinction_score`)
  - Is the score exactly 100? (`student_score == 100`)
  - Is the score below passing? (`student_score < passing_score`)

**Expected output**
```
Passed:        True
Distinction:   False
Perfect score: False
Below passing: False
```

**File:** `task_02.py`

---

## Task 3 — The access gate

**Scenario**
A secure office building has an automated gate that checks three conditions before allowing entry: the person must have a valid badge, be within working hours, and not be on the suspended list.

**Your task**
- Define: `has_badge = True`, `is_working_hours = True`, `is_suspended = False`
- Calculate `can_enter` using logical operators: must have badge AND be in working hours AND NOT be suspended
- Also calculate: `alert_security` = True if the person has no badge OR is suspended
- Print both results clearly

**Expected output**
```
Can enter building: True
Alert security:     False
```

**File:** `task_03.py`

---

## Task 4 — The unit converter

**Scenario**
A construction company works with both metric and imperial measurements. Their software must convert between kilometres and miles, and between kilograms and pounds, to communicate with international partners.

**Your task**
- Define: `distance_km = 42.195` (a marathon), `weight_kg = 75.0`
- Convert km to miles (1 km = 0.621371 miles) and round to 2 decimal places using `round()`
- Convert kg to pounds (1 kg = 2.20462 pounds) and round to 2 decimal places
- Cast the rounded mile result to `int` and print it as a whole number too
- Print all results clearly labelled

**Expected output**
```
Distance: 42.195 km = 26.22 miles (≈ 26 miles)
Weight:   75.0 kg = 165.35 pounds
```

**File:** `task_04.py`

---

## Task 5 — The odd or even detector

**Scenario**
A lottery system needs to classify ticket numbers. Even-numbered tickets go into one draw, odd-numbered tickets into another. The system also needs to check if a number is divisible by 5 for a special bonus prize.

**Your task**
- Define: `ticket_number = 347`
- Use the modulo operator to check if the ticket is even or odd
- Check if the ticket number is divisible by 5
- Print the ticket number, whether it is even or odd (as a True/False), and whether it qualifies for the bonus

**Expected output**
```
Ticket number: 347
Is even:       False
Is odd:        True
Bonus prize:   False
```

**File:** `task_05.py`

---

## Task 6 — The discount engine

**Scenario**
An online store applies discounts based on order value. The pricing team needs a script that takes an original price, applies a percentage discount, calculates how much was saved, and shows the final price — all using proper casting and arithmetic.

**Your task**
- Define: `original_price = "199.99"` (it comes as a string from the web form), `discount_percent = "15"`
- Cast both values to the correct numeric types
- Calculate: discount amount, final price, and the savings percentage message
- The final price must be rounded to 2 decimal places
- Print a formatted receipt

**Expected output**
```
Original price:  199.99 USD
Discount:        15%
You save:        30.0 USD
Final price:     169.99 USD
```

**File:** `task_06.py`

