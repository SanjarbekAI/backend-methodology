# L06 Tasks — While & For Loops

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The countdown timer

**Scenario**
A rocket launch control system displays a countdown before ignition. After the countdown reaches zero, it prints the launch message. If the countdown is aborted (simulated here by a variable), it exits early with a different message.

**Your task**
- Use a `while` loop to count down from 10 to 1, printing each number
- After the loop, print "🚀 Liftoff!"
- Add a variable `abort = False` — if you change it to `True`, the loop should `break` and print "⛔ Launch aborted." instead

**Expected output** (abort = False)
```
10... 9... 8... 7... 6... 5... 4... 3... 2... 1...
🚀 Liftoff!
```

**Expected output** (abort = True, break after count reaches 5)
```
10... 9... 8... 7... 6...
⛔ Launch aborted.
```

**File:** `task_01.py`

---

## Task 2 — The multiplication table

**Scenario**
A math tutoring app generates multiplication tables for students practicing their times tables. Each row shows all multiples of a number from 1 to 10, neatly formatted.

**Your task**
- Use nested `for` loops to print a full multiplication table for numbers 1 through 5
- Each row should be formatted: `1 x 1 = 1`, `1 x 2 = 2`, etc.
- Print a separator line (`---`) between each number's table

**Expected output**
```
--- Table of 1 ---
1 x 1 = 1
1 x 2 = 2
...
1 x 10 = 10
--- Table of 2 ---
2 x 1 = 2
...
```

**File:** `task_02.py`

---

## Task 3 — The even number collector

**Scenario**
A data filtering tool needs to scan a range of numbers and collect only the even ones, skipping the odd ones. It then prints a summary of how many were found.

**Your task**
- Loop through numbers 1 to 50 using a `for` loop
- Use `continue` to skip odd numbers
- Print each even number on the same line separated by spaces (hint: use `print(n, end=" ")`)
- After the loop, print a new line and then: "Total even numbers found: X"

**Expected output**
```
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 
Total even numbers found: 25
```

**File:** `task_03.py`

---

## Task 4 — The order processor

**Scenario**
A warehouse system processes a list of orders one by one. Each order has a status. The system prints each order being processed, but skips cancelled orders and stops entirely if it encounters a "HOLD" status (meaning warehouse operations are paused).

**Your task**
- Define a list of order statuses:
  `["pending", "pending", "cancelled", "pending", "HOLD", "pending", "pending"]`
- Loop through the list using `for` and a counter starting at 1
- If status is `"cancelled"` → print `"Order {n}: Skipped (cancelled)"` and `continue`
- If status is `"HOLD"` → print `"⚠️ HOLD signal received. Processing stopped."` and `break`
- Otherwise → print `"Order {n}: Processing..."`

**Expected output**
```
Order 1: Processing...
Order 2: Processing...
Order 3: Skipped (cancelled)
Order 4: Processing...
⚠️ HOLD signal received. Processing stopped.
```

**File:** `task_04.py`

---

## Task 5 — The PIN attempt system

**Scenario**
A mobile banking app allows a user to enter their PIN up to 3 times before locking the account. The system counts attempts and gives feedback after each wrong entry.

**Your task**
- Define: `correct_pin = "7749"`, `max_attempts = 3`
- Simulate 3 attempts using a list: `attempts = ["1234", "0000", "7749"]`
- Use a `while` loop with an attempt counter
- If the PIN matches → print "✅ Access granted." and `break`
- If not → print remaining attempts
- If all 3 fail → print "🔒 Account locked. Contact support."

**Expected output** (for attempts = ["1234", "0000", "7749"])
```
❌ Wrong PIN. 2 attempts remaining.
❌ Wrong PIN. 1 attempt remaining.
✅ Access granted.
```

**File:** `task_05.py`

---

## Task 6 — The star pattern printer

**Scenario**
A graphic design tool for a children's learning app needs to generate text-based triangle patterns that can be adjusted to different sizes. The developer writes a loop-based pattern generator.

**Your task**
- Use nested `for` loops to print two patterns:
  - Pattern 1: A right-angled triangle of `*` characters, 5 rows tall
  - Pattern 2: An upside-down triangle, also 5 rows

**Expected output**
```
Pattern 1:
*
**
***
****
*****

Pattern 2:
*****
****
***
**
*
```

**File:** `task_06.py`

