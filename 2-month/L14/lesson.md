# L14 — Closures & Higher-Order Functions

## Why this matters
Closures and higher-order functions are the bridge between "writing functions" and "thinking in functions." They are the foundation of decorators, callbacks, and functional programming — patterns you will see in every Python framework and library.

---

## Topics

## Closures — Functions that remember
A **closure** is a function defined inside another function that "remembers" the variables from its enclosing scope, even after the outer function has finished running.

```python
def make_multiplier(factor):        # outer function
    def multiply(number):           # inner function
        return number * factor      # 'factor' is remembered even after make_multiplier returns
    return multiply                 # return the inner function itself (not the result!)

double = make_multiplier(2)         # double is now a function that multiplies by 2
triple = make_multiplier(3)         # triple is a function that multiplies by 3

print(double(10))    # 20
print(triple(10))    # 30
print(double(7))     # 14
```

**Real use — a configurable tax calculator:**
```python
def make_tax_calculator(rate):
    def calculate(price):
        return price * (1 + rate / 100)
    return calculate

vat_12 = make_tax_calculator(12)
vat_20 = make_tax_calculator(20)

print(vat_12(100000))   # 112000.0
print(vat_20(100000))   # 120000.0
```

> ⚠️ **Common mistake:** Calling the returned function with parentheses at return time: `return multiply()` returns the result once. `return multiply` returns the function itself, which is what closures need.

---

## Nested functions — Functions inside functions
Any function can be defined inside another. This is useful for helper functions that are only relevant to one parent function.

```python
def process_order(order_data):
    def validate(data):                          # helper only needed here
        return all(key in data for key in ["item", "qty", "price"])

    def calculate_total(qty, price, discount=0):
        return qty * price * (1 - discount / 100)

    if not validate(order_data):
        return "Invalid order data"

    total = calculate_total(
        order_data["qty"],
        order_data["price"],
        order_data.get("discount", 0)
    )
    return f"Order total: {total:,.0f} sum"

order = {"item": "Laptop", "qty": 2, "price": 4500000, "discount": 10}
print(process_order(order))   # Order total: 8,100,000 sum
```

---

## `map()` — Apply a function to every item
`map(function, iterable)` applies a function to each element and returns a map object (convert with `list()`).

```python
prices = [100000, 250000, 80000, 175000]

# Apply 15% discount to every price
discounted = list(map(lambda p: p * 0.85, prices))
print(discounted)    # [85000.0, 212500.0, 68000.0, 148750.0]

# Convert a list of strings to integers
raw = ["10", "20", "30", "40"]
numbers = list(map(int, raw))   # int is a function too!
print(numbers)       # [10, 20, 30, 40]
```

---

## `filter()` — Keep only matching items
`filter(function, iterable)` keeps elements where the function returns `True`.

```python
scores = [88, 42, 95, 58, 73, 61, 90]

passing = list(filter(lambda s: s >= 60, scores))
print(passing)    # [88, 95, 73, 61, 90]

# Real use — filter active users
users = [
    {"name": "Ali", "active": True},
    {"name": "Sara", "active": False},
    {"name": "Layla", "active": True},
]
active_users = list(filter(lambda u: u["active"], users))
print([u["name"] for u in active_users])  # ["Ali", "Layla"]
```

---

## `reduce()` — Collapse a list to a single value
`reduce()` is in `functools`. It applies a function cumulatively to produce one final result.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, x: acc + x, numbers)   # 1+2=3, 3+3=6, 6+4=10, 10+5=15
print(total)     # 15

# Find the maximum without using max()
largest = reduce(lambda a, b: a if a > b else b, numbers)
print(largest)   # 5

# Real use — combine order amounts
order_amounts = [150000, 240000, 80000, 310000]
grand_total = reduce(lambda acc, amt: acc + amt, order_amounts)
print(grand_total)  # 780000
```

> ⚠️ **Common mistake:** Using `reduce()` for things that `sum()`, `max()`, or `min()` already do. Use `reduce()` only when there is no built-in alternative for your operation.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `def outer(): def inner(): ...` | Nested function | See closure example |
| `return inner` | Return function object (not result) | `return multiply` |
| `closure = outer(arg)` | Create a closure | `double = make_multiplier(2)` |
| `map(fn, iterable)` | Apply fn to each item | `map(int, ["1","2"])` |
| `filter(fn, iterable)` | Keep items where fn returns True | `filter(lambda x: x>0, lst)` |
| `from functools import reduce` | Import reduce | — |
| `reduce(fn, iterable)` | Fold list to one value | `reduce(lambda a,b: a+b, lst)` |
| `list(map(...))` | Convert map to list | `list(map(str, [1,2,3]))` |

---

## Task list

1. The configurable discount factory
2. The data pipeline
3. The grade filter and counter
4. The salary processor
5. The search factory

