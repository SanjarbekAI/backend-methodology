# L02 — Variables & Data Types

## Why this matters
Every piece of information a program works with — a user's name, their account balance, whether they are logged in — is stored in a variable. Understanding data types means you understand *what kind* of information you are working with, which prevents countless bugs before they happen.

---

## Topics

## Variable assignment — Giving names to data
A **variable** is a labelled box in your computer's memory. You give it a name, and you store something inside it. Python uses `=` to assign a value to a variable.

```python
name = "Layla"          # store the text "Layla" in a variable called name
age = 25                # store the number 25 in a variable called age
height = 1.72           # store the decimal number 1.72 in height
is_student = True       # store True or False in is_student

print(name)             # prints: Layla
print(age)              # prints: 25
```

**Naming rules:**
- Use lowercase letters and underscores: `user_name`, `total_price`
- Cannot start with a number: `2fast` ❌ → `fast2` ✅
- Cannot use reserved words: `if`, `for`, `class`, etc.

> ⚠️ **Common mistake:** Confusing `=` (assignment) with `==` (comparison). `x = 5` stores 5. `x == 5` asks "is x equal to 5?" — these are completely different.

---

## `int` — Whole numbers
Integers are numbers without a decimal point. They are used for counting things, IDs, ages, quantities.

```python
items_in_cart = 3       # number of products in a shopping cart
floor_number = 12       # floor of a building
temperature = -5        # negative integers are valid too

print(type(items_in_cart))  # <class 'int'> — type() tells you what type a variable is
```

> ⚠️ **Common mistake:** Storing a number as a string: `age = "25"` is NOT the same as `age = 25`. You cannot do math on `"25"`.

---

## `float` — Decimal numbers
Floats are numbers with a decimal point. Used for prices, measurements, percentages.

```python
price = 9.99            # product price
tax_rate = 0.18         # 18% tax
distance_km = 3.5       # distance in kilometres

print(type(price))      # <class 'float'>
```

> ⚠️ **Common mistake:** Expecting perfect decimal precision. `0.1 + 0.2` gives `0.30000000000000004` in Python due to how computers store floats. For money, use the `decimal` module (learned later).

---

## `str` — Text / strings
A string is any sequence of characters wrapped in quotes (single `'` or double `"`). Used for names, messages, addresses, anything textual.

```python
first_name = "Sara"             # double quotes work
last_name = 'Karimova'          # single quotes work the same way
email = "sara@example.com"      # can contain special characters
empty = ""                      # an empty string is valid

print(type(first_name))         # <class 'str'>
print(first_name + " " + last_name)  # joins strings together: Sara Karimova
```

> ⚠️ **Common mistake:** Forgetting quotes around text. `name = Sara` causes a `NameError` because Python thinks `Sara` is another variable.

---

## `bool` — True or False
Booleans represent one of exactly two values: `True` or `False`. They power every decision your program makes — every `if` statement uses a boolean under the hood.

```python
is_logged_in = True         # the user is currently logged in
has_paid = False            # the order has not been paid yet
is_admin = True

print(type(is_logged_in))   # <class 'bool'>
print(is_logged_in)         # True
```

> ⚠️ **Common mistake:** Writing `true` or `false` (lowercase). Python is case-sensitive — `True` and `False` must start with a capital letter.

---

## `type()` — Checking the type
`type()` is a built-in function that returns the data type of any value or variable. Extremely useful for debugging.

```python
x = 42
y = 3.14
z = "hello"
w = True

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(w))  # <class 'bool'>
```

---

## Dynamic typing — Python changes type for you
Python is **dynamically typed** — a variable can hold any type, and you can change it at any time. You never have to declare the type explicitly.

```python
data = 100          # data is an int
print(type(data))   # <class 'int'>

data = "hello"      # now data is a str — Python is fine with this
print(type(data))   # <class 'str'>

data = 3.14         # now it is a float
print(type(data))   # <class 'float'>
```

**Analogy:** Think of a variable like a whiteboard. You can erase what's on it and write something completely different. The whiteboard (variable name) stays the same — only the content changes.

> ⚠️ **Common mistake:** Accidentally overwriting a variable you still need. If you write `total = 0` and later `total = "done"`, your original number is gone forever.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `x = value` | Assigns a value to a variable | `age = 25` |
| `int` | Whole number type | `score = 100` |
| `float` | Decimal number type | `price = 9.99` |
| `str` | Text type (in quotes) | `name = "Ali"` |
| `bool` | True or False | `active = True` |
| `type(x)` | Returns the data type of x | `type(42)` → `<class 'int'>` |
| `x, y = 1, 2` | Assigns multiple variables at once | `a, b = 10, 20` |

---

## Task list

1. The student profile
2. The product listing
3. The type detective
4. The swap trick
5. The dynamic type experiment
6. The profile updater

