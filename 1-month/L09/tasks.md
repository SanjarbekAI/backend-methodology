# L09 Tasks — User Input & Error Handling

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The age registration form

**Scenario**
A gym's membership registration system asks a new member to enter their age. The system must validate that the input is a valid integer and that the age is within a realistic range (5–110). If not, it shows a clear error message.

**Your task**
- Use `input()` to ask: `"Enter your age: "`
- Wrap the conversion in `try/except` to catch `ValueError`
- If the age is outside 5–110, print a range error
- If valid, print: `"Welcome! You have registered as a [category] member."`
  - Under 18 → Junior
  - 18–60 → Standard
  - Over 60 → Senior

**Expected output** (input: 25)
```
Enter your age: 25
Welcome! You have registered as a Standard member.
```

**Expected output** (input: "abc")
```
Enter your age: abc
Error: Age must be a whole number.
```

**File:** `task_01.py`

---

## Task 2 — The calculator with guard

**Scenario**
A construction company's field app has a simple calculator that workers use to compute material quantities. The app must handle both non-numeric input and division-by-zero gracefully without crashing.

**Your task**
- Ask the user to enter two numbers and an operator (`+`, `-`, `*`, `/`)
- Perform the calculation
- Handle `ValueError` (non-numeric input) and `ZeroDivisionError` (dividing by zero)
- Use `finally` to always print: `"Calculation attempt complete."`

**Expected output** (input: 10, 4, /)
```
First number: 10
Second number: 4
Operator (+, -, *, /): /
Result: 10.0 / 4.0 = 2.5
Calculation attempt complete.
```

**Expected output** (input: 10, 0, /)
```
First number: 10
Second number: 0
Operator (+, -, *, /): /
Error: Cannot divide by zero.
Calculation attempt complete.
```

**File:** `task_02.py`

---

## Task 3 — The menu-driven app

**Scenario**
A small restaurant's ordering kiosk displays a menu and asks the customer to select an item by number. The system must handle invalid selections (non-integer or out-of-range) without crashing.

**Your task**
- Define a menu as a dictionary: `{1: "Burger", 2: "Pizza", 3: "Salad", 4: "Soup"}`
- Display the menu with prices (make up prices)
- Ask: `"Enter item number: "`
- Handle: `ValueError` (non-integer), and `KeyError` (number not in menu)
- If valid, print: `"You selected: [item] — [price] sum"`

**Expected output** (input: 2)
```
=== MENU ===
1. Burger  — 35,000 sum
2. Pizza   — 45,000 sum
3. Salad   — 25,000 sum
4. Soup    — 20,000 sum

Enter item number: 2
You selected: Pizza — 45,000 sum
```

**Expected output** (input: "five")
```
Enter item number: five
Error: Please enter a number from the menu.
```

**File:** `task_03.py`

---

## Task 4 — The stock lookup tool

**Scenario**
A pharmacy uses a dictionary to store medicine stock levels. A staff member types a medicine name to check availability. The system handles misspelled or unknown medicine names gracefully.

**Your task**
- Define a stock dictionary with at least 6 medicines and their quantities
- Ask: `"Enter medicine name: "`
- Convert input to title case before lookup (so "paracetamol" finds "Paracetamol")
- Use `try/except KeyError` to handle unknown medicines
- Print the quantity if found, or a "not in system" message if not

**Expected output** (input: "ibuprofen")
```
Enter medicine name: ibuprofen
Ibuprofen: 47 units in stock.
```

**Expected output** (input: "melatonin")
```
Enter medicine name: melatonin
Melatonin is not in our system.
```

**File:** `task_04.py`

---

## Task 5 — The safe list accessor

**Scenario**
A student exam system stores scores in a list. A teacher can look up any student's score by their position number (1-based, as displayed to non-programmers). The system must handle out-of-range numbers gracefully.

**Your task**
- Define: `scores = [88, 72, 95, 61, 83, 90, 55]`
- Ask: `"Enter student position (1–7): "`
- Convert to integer and adjust to 0-based index (`position - 1`)
- Handle `ValueError` (non-integer) and `IndexError` (out of range)
- Print the score if valid

**Expected output** (input: 3)
```
Enter student position (1-7): 3
Student 3 scored: 95
```

**Expected output** (input: 10)
```
Enter student position (1-7): 10
Error: Position 10 does not exist. Valid range is 1–7.
```

**File:** `task_05.py`

---

## Task 6 — The robust data entry loop

**Scenario**
A data entry operator at a logistics company needs to record the weights of 3 packages. The system must keep asking for each weight until a valid positive number is entered — it never crashes and never accepts invalid input.

**Your task**
- Use a `while True` loop for each of 3 packages
- Inside the loop: ask for the weight, try to convert to float
- If `ValueError` → print error and loop again
- If the number is ≤ 0 → print "Weight must be positive" and loop again
- If valid → store the weight and move to the next package
- After all 3 are entered: print the total weight and average

**Expected output**
```
=== Package 1 ===
Enter weight (kg): abc
Error: Please enter a valid number.
Enter weight (kg): -2
Error: Weight must be positive.
Enter weight (kg): 12.5
✓ Recorded: 12.5 kg

=== Package 2 ===
Enter weight (kg): 8.0
✓ Recorded: 8.0 kg

=== Package 3 ===
Enter weight (kg): 15.3
✓ Recorded: 15.3 kg

Total weight:   35.8 kg
Average weight: 11.93 kg
```

**File:** `task_06.py`

