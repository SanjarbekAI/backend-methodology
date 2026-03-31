# L04 — Strings & Formatting

## Why this matters
Almost every program displays text to a user. Whether it is a receipt, an error message, a report, or a search result — you are formatting and manipulating strings. Mastering strings means your output looks professional and your data processing is clean.

---

## Topics

## String slicing — Cutting out pieces
A string is a sequence of characters. Each character has an **index** (position number) starting at 0. You can extract any portion of a string using **slicing**.

```python
email = "layla@example.com"

# Indexing — get one character
print(email[0])       # l — first character (index 0)
print(email[-1])      # m — last character (negative index counts from end)

# Slicing — get a range: [start:stop]  (stop is NOT included)
print(email[0:5])     # layla — characters 0,1,2,3,4
print(email[6:])      # example.com — from index 6 to the end
print(email[:5])      # layla — from start up to (not including) index 5
print(email[::2])     # every second character
print(email[::-1])    # reverses the string: moc.elpmaxe@ayal
```

> ⚠️ **Common mistake:** Forgetting that the stop index is exclusive. `"hello"[0:3]` gives `"hel"`, not `"hell"`. The character at index 3 is NOT included.

---

## String methods — Built-in tools for text
Python strings come with dozens of built-in methods (functions). Here are the most essential ones:

```python
text = "  Hello, World!  "

# Case methods
print(text.upper())           # "  HELLO, WORLD!  "
print(text.lower())           # "  hello, world!  "
print(text.title())           # "  Hello, World!  "

# Whitespace
print(text.strip())           # "Hello, World!"  — removes leading/trailing spaces
print(text.lstrip())          # "Hello, World!  " — removes only left spaces
print(text.rstrip())          # "  Hello, World!" — removes only right spaces

# Search & replace
name = "Sara Karimova"
print(name.replace("Sara", "Layla"))  # "Layla Karimova"
print(name.find("Kar"))               # 5 — index where "Kar" starts (-1 if not found)
print(name.count("a"))                # 3 — how many times "a" appears

# Check content
code = "AB1042"
print(code.startswith("AB"))  # True
print(code.endswith("42"))    # True
print("12345".isdigit())      # True — all characters are digits
print("hello".isalpha())      # True — all characters are letters

# Split and join
csv = "apple,banana,cherry"
fruits = csv.split(",")        # ["apple", "banana", "cherry"] — splits into list
print(" | ".join(fruits))      # "apple | banana | cherry" — joins list back to string
```

> ⚠️ **Common mistake:** Forgetting that string methods return a **new string** — they do NOT modify the original. `name.upper()` gives a new string; `name` is still unchanged.

---

## f-strings — The modern way to format strings
An **f-string** (formatted string literal) lets you embed variables directly inside a string. Add `f` before the opening quote and wrap variables in `{}`.

```python
name = "Rustam"
age = 24
salary = 4500000.0

# Basic f-string
print(f"Hello, {name}! You are {age} years old.")
# Hello, Rustam! You are 24 years old.

# Expressions inside {}
print(f"In 5 years you will be {age + 5}.")
# In 5 years you will be 29.

# Number formatting
print(f"Salary: {salary:,.0f} sum")   # :,.0f = comma separator, 0 decimal places
# Salary: 4,500,000 sum

print(f"Price: {9.9967:.2f} USD")     # :.2f = exactly 2 decimal places
# Price: 10.00 USD

print(f"{'Centered':^20}")            # :^20 = center in a 20-char wide field
#        Centered        
```

> ⚠️ **Common mistake:** Using the old `%` formatting or `.format()` style. Both still work, but f-strings are cleaner, faster, and the current standard for Python 3.6+.

---

## Multi-line strings — Text that spans several lines
Triple quotes (`"""` or `'''`) let you write strings that span multiple lines without needing `\n` everywhere.

```python
# Multi-line string — preserves line breaks
message = """
Dear Kamola,

Your order #10842 has been shipped.
Expected delivery: 2–3 business days.

Thank you for shopping with us.
"""
print(message)

# Useful for SQL queries, long messages, email templates
query = """
SELECT name, email
FROM users
WHERE is_active = True
ORDER BY name
"""
print(query)
```

> ⚠️ **Common mistake:** Not realizing that the indentation inside triple-quoted strings is part of the string. Extra spaces inside will appear in the output.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `s[i]` | Character at index i | `"hello"[1]` → `"e"` |
| `s[a:b]` | Slice from a to b (b excluded) | `"hello"[1:3]` → `"el"` |
| `s[::-1]` | Reverse a string | `"abc"[::-1]` → `"cba"` |
| `s.upper()` | All uppercase | `"hi".upper()` → `"HI"` |
| `s.lower()` | All lowercase | `"HI".lower()` → `"hi"` |
| `s.strip()` | Remove leading/trailing spaces | `" hi ".strip()` → `"hi"` |
| `s.replace(a, b)` | Replace a with b | `"cat".replace("c","b")` → `"bat"` |
| `s.split(sep)` | Split into a list | `"a,b".split(",")` → `["a","b"]` |
| `sep.join(list)` | Join list into string | `",".join(["a","b"])` → `"a,b"` |
| `s.find(sub)` | Index of first match (-1 if none) | `"hello".find("ll")` → `2` |
| `f"{var}"` | f-string formatting | `f"Hi {name}"` |
| `f"{num:.2f}"` | Float with 2 decimal places | `f"{3.1:.2f}"` → `"3.10"` |
| `"""..."""` | Multi-line string | `"""line1\nline2"""` |

---

## Task list

1. The email parser
2. The name formatter
3. The product label generator
4. The password validator
5. The report card formatter
6. The message template engine

