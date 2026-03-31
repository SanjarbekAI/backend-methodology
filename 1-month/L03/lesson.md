# L03 — Numbers, Casting & Operators

## Why this matters
Operators and casting are the building blocks of every calculation your program will ever make — from calculating a shopping cart total to computing a loan payment or checking whether a user entered a valid age. Without them, your variables just sit there doing nothing.

---

## Topics

## Arithmetic operators — Doing math
Python supports all standard math operations. Think of your program as a calculator that can work with variables.

```python
a = 20
b = 6

print(a + b)    # addition:        26
print(a - b)    # subtraction:     14
print(a * b)    # multiplication:  120
print(a / b)    # division:        3.3333... (always returns float)
print(a // b)   # floor division:  3 (drops the decimal — rounds down)
print(a % b)    # modulo:          2 (the remainder after dividing 20 by 6)
print(a ** b)   # exponentiation:  64000000 (20 to the power of 6)
```

**Real use — calculating a taxi fare:**
```python
distance_km = 12
rate_per_km = 1500       # price in sum per km
base_fare = 3000         # starting price

total = base_fare + (distance_km * rate_per_km)
print("Total fare:", total, "sum")   # Total fare: 21000 sum
```

> ⚠️ **Common mistake:** Using `/` when you want a whole number result. `7 / 2` gives `3.5`, not `3`. Use `//` for whole-number (integer) division.

---

## Comparison operators — Asking yes/no questions
Comparison operators compare two values and always return `True` or `False`.

```python
x = 10
y = 20

print(x == y)   # equal to:               False
print(x != y)   # not equal to:           True
print(x > y)    # greater than:           False
print(x < y)    # less than:              True
print(x >= 10)  # greater than or equal:  True
print(x <= 9)   # less than or equal:     False
```

> ⚠️ **Common mistake:** Using `=` instead of `==` to compare values. `if x = 5:` is a syntax error. `if x == 5:` is correct.

---

## Logical operators — Combining conditions
Logical operators combine multiple comparisons into one.

```python
age = 22
has_ticket = True

# and → both conditions must be True
print(age >= 18 and has_ticket)    # True — age is 22 AND has ticket

# or → at least one condition must be True
print(age >= 18 or has_ticket)     # True

# not → flips True to False, False to True
print(not has_ticket)              # False (flips True)

# Real example: access control check
is_admin = False
is_verified = True
can_access = is_admin or is_verified
print("Access granted:", can_access)    # Access granted: True
```

**Operator truth table:**

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

> ⚠️ **Common mistake:** Writing `and` or `or` as `&&` or `||` (those are from JavaScript/C). Python uses the words `and`, `or`, `not`.

---

## Type casting — Converting between types
Sometimes you have a value of one type but need it in another. **Casting** converts a value to a different type using built-in functions.

```python
# int() → convert to integer
print(int(3.9))      # 3  ← truncates (does NOT round, just drops decimal)
print(int("42"))     # 42 ← converts string to int
print(int(True))     # 1  ← True is 1, False is 0

# float() → convert to float
print(float(5))      # 5.0
print(float("3.14")) # 3.14

# str() → convert to string
print(str(100))      # "100"
print(str(3.14))     # "3.14"
print(str(True))     # "True"
```

**Real example — user input is always a string:**
```python
raw_input = "25"             # imagine this came from the user typing
age = int(raw_input)         # convert to int so we can do math
next_year_age = age + 1      # now this works!
print("Next year you will be", next_year_age)  # Next year you will be 26
```

> ⚠️ **Common mistake:** Trying to cast something that cannot be converted. `int("hello")` raises a `ValueError`. Always make sure the value makes sense before casting.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `a + b` | Addition | `5 + 3` → `8` |
| `a - b` | Subtraction | `10 - 4` → `6` |
| `a * b` | Multiplication | `3 * 4` → `12` |
| `a / b` | Division (float result) | `7 / 2` → `3.5` |
| `a // b` | Floor division (int result) | `7 // 2` → `3` |
| `a % b` | Modulo (remainder) | `10 % 3` → `1` |
| `a ** b` | Exponentiation | `2 ** 8` → `256` |
| `==`, `!=` | Equal / not equal | `x == 5` |
| `>`, `<`, `>=`, `<=` | Comparisons | `age >= 18` |
| `and`, `or`, `not` | Logical operators | `a > 0 and b > 0` |
| `int(x)` | Convert to integer | `int("10")` → `10` |
| `float(x)` | Convert to float | `float(5)` → `5.0` |
| `str(x)` | Convert to string | `str(42)` → `"42"` |

---

## Task list

1. The invoice calculator
2. The grade checker
3. The access gate
4. The unit converter
5. The odd or even detector
6. The discount engine

