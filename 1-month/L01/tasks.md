# L01 Tasks — Syntax, Output & Comments

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — Hello, world!

**Scenario**
You just got hired as a junior developer at a startup. Your team lead asks you to write the very first line of the new project as a tradition — every project at this company starts with a greeting printed to the console.

**Your task**
- Print exactly the text: `Hello, world!`
- On the next line, print: `My first Python program.`

**Expected output**
```
Hello, world!
My first Python program.
```

**File:** `task_01.py`

---

## Task 2 — Personal introduction card

**Scenario**
A local tech community is building a directory of its members. Each member must submit a small script that prints their personal introduction card to the terminal.

**Your task**
- Print your name on one line, labelled: `Name: ...`
- Print your age on the next line, labelled: `Age: ...`
- Print your city on the next line, labelled: `City: ...`
- Print a short one-sentence bio on the last line, labelled: `Bio: ...`

**Expected output**
```
Name: Ali Hassan
Age: 22
City: Tashkent
Bio: I am learning Python to become a backend developer.
```
*(Use your own information.)*

**File:** `task_02.py`

---

## Task 3 — The receipt printer

**Scenario**
A small café owner wants a simple script that prints a formatted receipt for a coffee order. The receipt must look clean and professional when printed in the terminal.

**Your task**
- Print a top border line using `=` characters
- Print the café name centered between the borders
- Print three menu items with their prices (make them up)
- Print a bottom border line
- Use at least one inline comment explaining what each section does

**Expected output**
```
==============================
        Sunrise Café
==============================
Espresso           2.50 USD
Croissant          1.80 USD
Orange Juice       3.00 USD
==============================
```

**File:** `task_03.py`

---

## Task 4 — The commented blueprint

**Scenario**
A senior developer at a software company is creating a blueprint (template) file that junior developers will fill in later. The file must clearly describe what each section is for using comments, without running any actual code yet.

**Your task**
- Write a file with 5 sections, each marked with a comment describing what will go there
  - Section 1: Import statements
  - Section 2: Configuration variables
  - Section 3: Main logic
  - Section 4: Output / display
  - Section 5: Program entry point
- Under each comment, write one `print()` placeholder that says what that section will eventually do
- Add a multi-line docstring at the top of the file describing the program's purpose

**Expected output**
```
[Imports will go here]
[Config will go here]
[Main logic will go here]
[Output will go here]
[Entry point will go here]
```

**File:** `task_04.py`

---

## Task 5 — The story printer

**Scenario**
A children's app developer needs to display a short 5-line story in the terminal. The story must appear with blank lines between paragraphs so it is easy to read.

**Your task**
- Print a story title
- Print a blank line (hint: `print()` with no arguments prints a blank line)
- Print lines 1 and 2 of the story
- Print another blank line
- Print lines 3, 4, and 5 of the story
- Make the story about anything you like — it just needs to make sense

**Expected output**
```
The Lost Key

A young engineer named Layla lost her office key.
She searched everywhere — her bag, her desk, her car.

Finally, she checked her coat pocket.
The key was there all along.
She laughed and made a copy the very same day.
```

**File:** `task_05.py`

---

## Task 6 — The broken code fixer

**Scenario**
A new intern at a software company submitted their first Python file, but it has several syntax and structural errors. Your job as the senior developer is to identify and fix every error so the file runs correctly.

**Your task**
- Copy the broken code below into your file exactly as shown
- Fix every error (there are 5 errors total)
- Add a comment next to each fix explaining what was wrong

**Broken code to fix:**
```python
"""
Program: Company Greeter
Purpose: Print a welcome message for new employees
"""

Print("Welcome to TechCorp!")       # Error 1
print "Please read the handbook."   # Error 2
print("Your desk is on floor 3")
    print("Enjoy your first day!")  # Error 3
# print("The cafeteria opens at 8") # Error 4 — this line should actually run
print("See you tomorrow!"           # Error 5
```

**Expected output (after fixing):**
```
Welcome to TechCorp!
Please read the handbook.
Your desk is on floor 3
Enjoy your first day!
The cafeteria opens at 8
See you tomorrow!
```

**File:** `task_06.py`

