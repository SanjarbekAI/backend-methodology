# L06 — While & For Loops

## Why this matters
Imagine sending a personalized email to 50,000 customers one by one — manually. Loops are what make computers powerful: they do repetitive work in milliseconds. Every real application — generating reports, processing orders, scanning files — relies on loops.

---

## Topics

## `while` loop — Repeat until a condition is False
A `while` loop keeps running as long as its condition remains `True`. It is used when you don't know in advance how many times you need to repeat something.

```python
countdown = 5

while countdown > 0:           # keep looping while countdown is greater than 0
    print(f"T-minus {countdown}")  # print current value
    countdown -= 1             # decrease by 1 each time (IMPORTANT — avoid infinite loop!)

print("Liftoff!")
# Output: T-minus 5, T-minus 4, T-minus 3, T-minus 2, T-minus 1, Liftoff!
```

**Real example — ATM PIN retry:**
```python
attempts = 0
correct_pin = "1234"

while attempts < 3:
    pin = "9999"                         # imagine this is user input
    if pin == correct_pin:
        print("Access granted!")
        break                            # exit the loop immediately
    else:
        attempts += 1
        print(f"Wrong PIN. {3 - attempts} attempts left.")

if attempts == 3:
    print("Card blocked.")
```

> ⚠️ **Common mistake:** Creating an **infinite loop** by forgetting to update the variable the condition depends on. If `countdown` never decreases, the loop runs forever and freezes your program. Always make sure the condition can eventually become False.

---

## `for` loop — Repeat a known number of times
A `for` loop iterates over a sequence (a range of numbers, a list, a string, etc.). Use it when you know what you are looping over.

```python
# Loop over a range of numbers
for i in range(5):                 # i = 0, 1, 2, 3, 4
    print(f"Item {i}")

# Loop over a string — each character at a time
for letter in "Python":
    print(letter)                  # P, y, t, h, o, n (each on a new line)

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")
```

> ⚠️ **Common mistake:** Modifying the list you are iterating over inside the loop. This causes unpredictable behavior. If you need to modify a list, iterate over a copy: `for item in my_list[:]`.

---

## `range()` — Generating number sequences
`range()` generates a sequence of numbers without storing them all in memory.

```python
range(5)          # 0, 1, 2, 3, 4  (stop only)
range(1, 6)       # 1, 2, 3, 4, 5  (start, stop)
range(0, 20, 5)   # 0, 5, 10, 15   (start, stop, step)
range(10, 0, -1)  # 10, 9, 8, ..., 1  (count down)

# Common pattern — loop n times
for i in range(1, 6):
    print(f"Line {i}")   # Line 1, Line 2, Line 3, Line 4, Line 5
```

> ⚠️ **Common mistake:** `range(5)` gives 0–4 (5 items). If you want 1–5, use `range(1, 6)`. The stop value is **never** included.

---

## `break`, `continue`, `pass` — Controlling the flow
These three keywords give you fine-grained control inside loops.

```python
# break — exit the loop immediately
for n in range(10):
    if n == 5:
        break              # stop the loop when n reaches 5
    print(n)               # prints 0, 1, 2, 3, 4

# continue — skip the rest of this iteration, go to next
for n in range(10):
    if n % 2 == 0:
        continue           # skip even numbers
    print(n)               # prints 1, 3, 5, 7, 9 (odd numbers only)

# pass — do nothing (a placeholder)
for n in range(5):
    if n == 3:
        pass               # placeholder — we'll add code here later
    print(n)               # prints 0, 1, 2, 3, 4 (pass doesn't skip anything)
```

> ⚠️ **Common mistake:** Confusing `break` and `continue`. `break` exits the whole loop. `continue` only skips the current iteration and jumps to the next one.

---

## Nested loops — Loops inside loops
A loop can be placed inside another loop. The inner loop runs completely for every single iteration of the outer loop.

```python
# Multiplication table — 3x3
for row in range(1, 4):          # outer: rows 1, 2, 3
    for col in range(1, 4):      # inner: cols 1, 2, 3 (runs 3 times per row)
        print(f"{row} × {col} = {row * col}")
    print("---")                 # separator after each row
```

**Output:**
```
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3
---
2 × 1 = 2
...
```

> ⚠️ **Common mistake:** Losing track of which loop `break` belongs to. `break` only exits the **innermost** loop it is in — not the outer one.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `while condition:` | Loop while condition is True | `while x > 0:` |
| `for var in iterable:` | Loop over each item | `for i in range(5):` |
| `range(n)` | Numbers 0 to n-1 | `range(5)` → 0,1,2,3,4 |
| `range(a, b)` | Numbers a to b-1 | `range(1, 6)` → 1–5 |
| `range(a, b, step)` | With a step | `range(0, 10, 2)` → 0,2,4,6,8 |
| `break` | Exit the loop immediately | `if done: break` |
| `continue` | Skip current iteration | `if skip: continue` |
| `pass` | Do nothing (placeholder) | `if x: pass` |
| `for i, v in enumerate(lst)` | Loop with index and value | `enumerate(["a","b"])` |

---

## Task list

1. The countdown timer
2. The multiplication table
3. The even number collector
4. The order processor
5. The PIN attempt system
6. The star pattern printer

