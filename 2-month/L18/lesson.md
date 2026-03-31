# L18 — Iterators, Dates & Math

## Why this matters
Scheduling a meeting, calculating a deadline, finding the next billing date, measuring elapsed time — date and time operations appear in almost every real application. Understanding iterators deepens your model of how Python loops work, and the `math` module eliminates the need to reinvent standard computations.

---

## Topics

## `iter()` and `next()` — How loops actually work
Under the hood, every `for` loop uses the **iterator protocol**. An **iterator** is an object with a `__next__()` method that produces one value at a time.

```python
# Any iterable can be turned into an iterator manually
fruits = ["apple", "banana", "cherry"]
it = iter(fruits)           # create an iterator from the list

print(next(it))    # "apple"  — get first item
print(next(it))    # "banana" — get second item
print(next(it))    # "cherry" — get third item
# print(next(it)) ← StopIteration — iterator is exhausted

# A for loop does this automatically:
for fruit in fruits:           # Python calls iter(), then next() repeatedly
    print(fruit)               # until StopIteration is raised
```

**Custom iterator — generating Fibonacci numbers:**
```python
class FibIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self            # an iterator returns itself

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

for n in FibIterator(50):
    print(n, end=" ")     # 0 1 1 2 3 5 8 13 21 34
```

> ⚠️ **Common mistake:** Calling `next()` on a list directly. Lists are **iterable** but not **iterators**. You must call `iter(lst)` first to get an iterator from them.

---

## `datetime` module — Working with dates and times
```python
import datetime

# Current date and time
now = datetime.datetime.now()
print(now)                         # 2026-03-30 14:25:07.123456

today = datetime.date.today()
print(today)                       # 2026-03-30

# Creating specific dates
birthday = datetime.date(1999, 7, 15)
meeting = datetime.datetime(2026, 4, 5, 10, 30)   # year, month, day, hour, minute

# Date arithmetic with timedelta
from datetime import timedelta
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
deadline = today + timedelta(days=30)

print(f"Tomorrow: {tomorrow}")
print(f"Deadline: {deadline}")

# Difference between dates
days_until_deadline = (deadline - today).days
print(f"Days until deadline: {days_until_deadline}")
```

> ⚠️ **Common mistake:** Trying to subtract two `datetime` objects from different types (e.g., `date` vs `datetime`). They must be the same type. Use `.date()` to convert a `datetime` to just a `date`.

---

## Date formatting — `strftime` and `strptime`
```python
from datetime import datetime

now = datetime.now()

# strftime — format a datetime AS a string
print(now.strftime("%d/%m/%Y"))           # 30/03/2026
print(now.strftime("%B %d, %Y"))          # March 30, 2026
print(now.strftime("%Y-%m-%d %H:%M"))     # 2026-03-30 14:25

# strptime — PARSE a string INTO a datetime
date_str = "15 July 1999"
parsed = datetime.strptime(date_str, "%d %B %Y")
print(parsed)                              # 1999-07-15 00:00:00
print(type(parsed))                        # <class 'datetime.datetime'>
```

**Common format codes:**

| Code | Meaning | Example |
|---|---|---|
| `%Y` | 4-digit year | 2026 |
| `%m` | Month (zero-padded) | 03 |
| `%B` | Full month name | March |
| `%d` | Day (zero-padded) | 30 |
| `%H` | Hour 24h | 14 |
| `%M` | Minutes | 25 |

---

## `math` module — Mathematical operations
```python
import math

print(math.sqrt(144))      # 12.0 — square root
print(math.pi)             # 3.141592653589793
print(math.e)              # 2.718281828459045 — Euler's number
print(math.ceil(4.1))      # 5  — round UP always
print(math.floor(4.9))     # 4  — round DOWN always
print(math.abs(-7))        # use built-in abs(-7) = 7 (not in math module)
print(math.pow(2, 10))     # 1024.0 — power (same as 2**10 but returns float)
print(math.log(100, 10))   # 2.0 — log base 10 of 100
print(math.factorial(5))   # 120
print(math.gcd(48, 18))    # 6  — greatest common divisor
print(math.inf)            # infinity
print(math.isfinite(math.inf))  # False
```

> ⚠️ **Common mistake:** Using `math.round()` — it doesn't exist. Use the built-in `round()`. Also `math.abs()` doesn't exist — use built-in `abs()`.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `iter(iterable)` | Create an iterator | `it = iter([1,2,3])` |
| `next(iterator)` | Get next value | `next(it)` → `1` |
| `datetime.date.today()` | Today's date | `today = date.today()` |
| `datetime.datetime.now()` | Current date + time | `now = datetime.now()` |
| `timedelta(days=n)` | A duration of n days | `today + timedelta(days=7)` |
| `dt.strftime(fmt)` | Format datetime to string | `now.strftime("%d/%m/%Y")` |
| `datetime.strptime(s, fmt)` | Parse string to datetime | `strptime("30/03/2026", "%d/%m/%Y")` |
| `math.sqrt(x)` | Square root | `math.sqrt(25)` → `5.0` |
| `math.ceil(x)` | Round up | `math.ceil(3.1)` → `4` |
| `math.floor(x)` | Round down | `math.floor(3.9)` → `3` |
| `math.factorial(n)` | n! | `math.factorial(5)` → `120` |
| `math.gcd(a, b)` | Greatest common divisor | `math.gcd(12, 8)` → `4` |

---

## Task list

1. The subscription expiry checker
2. The age calculator
3. The delivery scheduler
4. The circle geometry tool
5. The event countdown

