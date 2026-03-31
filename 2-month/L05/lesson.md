# L16 — Comprehensions & Functional Style

## Why this matters
Comprehensions let you write transformations and filters in a single, readable line. They are one of the most loved Python features — used constantly in data processing, API development, and scripting. Mastering them makes your code both shorter and more expressive.

---

## Topics

## List comprehensions — Transform lists elegantly
A **list comprehension** is a concise way to create a new list by transforming or filtering another iterable.

```python
# Basic form: [expression for item in iterable]
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(1, 20) if x % 2 == 0]
print(evens)     # [2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transform and filter together
prices = [120000, 45000, 890000, 230000, 67000]
expensive = [p * 0.9 for p in prices if p > 100000]   # 10% off items over 100k
print(expensive)    # [108000.0, 801000.0, 207000.0]

# Real use — extract names from list of dicts
users = [{"name": "Ali", "active": True}, {"name": "Sara", "active": False}, {"name": "Layla", "active": True}]
active_names = [u["name"] for u in users if u["active"]]
print(active_names)    # ['Ali', 'Layla']
```

> ⚠️ **Common mistake:** Writing overly complex comprehensions with nested logic. If a comprehension takes more than a few seconds to understand, rewrite it as a regular loop. Readability always wins.

---

## Dict comprehensions — Build dicts in one line
```python
# Basic form: {key_expr: value_expr for item in iterable}
names = ["laptop", "mouse", "keyboard"]
prices = [8500000, 120000, 350000]

# Build a dict from two lists
catalog = {name: price for name, price in zip(names, prices)}
print(catalog)
# {'laptop': 8500000, 'mouse': 120000, 'keyboard': 350000}

# Transform an existing dict
discounted = {item: price * 0.85 for item, price in catalog.items()}
print(discounted)

# Filter a dict — keep only items under 500,000
affordable = {item: price for item, price in catalog.items() if price < 500000}
print(affordable)   # {'mouse': 120000, 'keyboard': 350000}
```

> ⚠️ **Common mistake:** Accidentally creating a dict with duplicate keys. If your `key_expr` produces the same key twice, the second value silently overwrites the first.

---

## Set comprehensions — Deduplicated results in one line
```python
# Basic form: {expression for item in iterable}
text = "hello world"
unique_letters = {ch for ch in text if ch != " "}
print(unique_letters)    # {'h', 'e', 'l', 'o', 'w', 'r', 'd'} — order varies

# Unique domains from email list
emails = ["ali@gmail.com", "sara@mail.ru", "bob@gmail.com", "layla@yahoo.com"]
domains = {e.split("@")[1] for e in emails}
print(domains)    # {'gmail.com', 'mail.ru', 'yahoo.com'}
```

---

## Generator comprehensions — Lazy evaluation
```python
# Basic form: (expression for item in iterable)  — uses () not []
total = sum(x ** 2 for x in range(1000))    # no list created — memory-efficient
print(total)     # 332833500

# Compare: list comp creates full list
lst = [x ** 2 for x in range(1000000)]     # 8 MB in memory

# Generator creates nothing until needed
gen = (x ** 2 for x in range(1000000))    # almost no memory
first = next(gen)                          # compute only the first value
```

---

## Conditional comprehensions — If-else inside the expression
```python
# if-else in the expression (not a filter — transforms every item)
scores = [88, 42, 95, 58, 73]
labels = ["Pass" if s >= 60 else "Fail" for s in scores]
print(labels)    # ['Pass', 'Fail', 'Pass', 'Fail', 'Pass']

# Real use — categorize orders
orders = [{"id": 1, "amount": 150000}, {"id": 2, "amount": 950000}, {"id": 3, "amount": 75000}]
tagged = [
    {**order, "tier": "Premium" if order["amount"] > 500000 else "Standard"}
    for order in orders
]
print(tagged)
```

> ⚠️ **Common mistake:** Confusing the two types of `if` in comprehensions:
> - **Filter** (at the end): `[x for x in lst if x > 0]` — skips items that don't match
> - **Ternary** (in the expression): `[x if x > 0 else 0 for x in lst]` — transforms every item

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `[expr for x in it]` | List comprehension | `[x*2 for x in range(5)]` |
| `[expr for x in it if cond]` | List comp with filter | `[x for x in lst if x>0]` |
| `[a if cond else b for x in it]` | List comp with ternary | `["Y" if x>0 else "N" for x in lst]` |
| `{k: v for x in it}` | Dict comprehension | `{n: n**2 for n in range(5)}` |
| `{expr for x in it}` | Set comprehension | `{x%3 for x in range(10)}` |
| `(expr for x in it)` | Generator expression | `sum(x**2 for x in range(100))` |
| `zip(a, b)` | Pair two iterables | `zip(keys, values)` |

---

## Task list

1. The price transformer
2. The inventory filter
3. The student grade tagger
4. The email domain analyzer
5. The sales summary builder

