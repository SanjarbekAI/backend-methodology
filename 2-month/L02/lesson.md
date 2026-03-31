# L13 — Functions: Advanced

## Why this matters
Real-world functions need to be flexible. A logging function should work whether you pass one message or ten. A data formatter should have sensible defaults but still let you customize it. These advanced function features let you build APIs that are both powerful and easy to use.

---

## Topics

## `*args` — Variable positional arguments
`*args` lets a function accept **any number of positional arguments**. They arrive as a tuple inside the function.

```python
def calculate_total(*prices):    # *prices collects all positional args into a tuple
    return sum(prices)

print(calculate_total(100, 200))             # 300
print(calculate_total(50, 75, 125, 250))     # 500
print(calculate_total(9.99))                 # 9.99

# Real use — a logging function that accepts any number of messages
def log(*messages):
    for msg in messages:
        print(f"[LOG] {msg}")

log("Server started", "Port: 8000", "Workers: 4")
```

> ⚠️ **Common mistake:** Placing parameters after `*args`. Regular parameters must come BEFORE `*args`. `def f(a, b, *args)` is valid. `def f(*args, b)` creates a keyword-only parameter (advanced use).

---

## `**kwargs` — Variable keyword arguments
`**kwargs` lets a function accept **any number of keyword arguments**. They arrive as a dictionary inside the function.

```python
def create_profile(**details):      # **details collects all keyword args into a dict
    for key, value in details.items():
        print(f"{key}: {value}")

create_profile(name="Layla", age=25, city="Tashkent", role="developer")
# name: Layla
# age: 25
# city: Tashkent
# role: developer

# Combining args and kwargs
def build_request(method, url, *headers, **params):
    print(f"{method} {url}")
    print("Headers:", headers)
    print("Params:", params)

build_request("GET", "/api/users", "Auth: Bearer xyz", page=1, limit=20)
```

> ⚠️ **Common mistake:** The names `args` and `kwargs` are just conventions — the `*` and `**` are what matter. `*data` and `**options` work exactly the same. Use descriptive names when it helps clarity.

---

## Default parameters — Optional arguments with fallback values
Default parameters let callers skip arguments they don't need to customize.

```python
def send_email(to, subject, body, priority="normal", html=False):
    print(f"To: {to}")
    print(f"Subject: {subject} [{priority}]")
    print(f"HTML: {html}")
    print(f"Body: {body}")

# Call with only required arguments
send_email("ali@mail.com", "Meeting", "See you at 9 AM.")
# priority defaults to "normal", html defaults to False

# Override defaults selectively
send_email("sara@mail.com", "URGENT", "System down!", priority="high", html=True)
```

> ⚠️ **Common mistake:** Using a mutable default (like a list or dict) as a default parameter. `def f(lst=[])` is a famous Python trap — the list is shared across all calls. Use `None` and create inside the function:
> ```python
> def f(lst=None):
>     if lst is None:
>         lst = []
> ```

---

## Keyword arguments — Explicit, readable calls
Any function parameter can be passed as a keyword argument. This makes calls more readable and order-independent.

```python
def create_order(customer, product, quantity, discount=0):
    total = quantity * 50000 * (1 - discount / 100)
    print(f"{customer}: {quantity}x {product} = {total:,.0f} sum")

# Positional — must match order
create_order("Rustam", "Laptop Stand", 2)

# Keyword — order doesn't matter, meaning is clear
create_order(product="Laptop Stand", customer="Layla", quantity=1, discount=10)
```

---

## Lambda functions — One-line throwaway functions
A **lambda** is a small anonymous function written on a single line. Perfect for short operations passed to other functions.

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2
print(square(5))             # 25

# Most useful when passed directly to other functions
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))                          # [1, 1, 2, 3, 4, 5, 6, 9]

products = [{"name": "A", "price": 300}, {"name": "B", "price": 100}, {"name": "C", "price": 200}]
sorted_products = sorted(products, key=lambda p: p["price"])
print(sorted_products)       # sorted by price: B, C, A

# With min/max
cheapest = min(products, key=lambda p: p["price"])
print(cheapest["name"])      # B
```

> ⚠️ **Common mistake:** Using lambda for complex logic. If you need more than one expression, use a regular `def` function. Lambdas are for simple, readable one-liners only.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `def f(*args):` | Accept any number of positional args | `def total(*prices):` |
| `def f(**kwargs):` | Accept any number of keyword args | `def profile(**info):` |
| `def f(x, y=10):` | Default parameter value | `def power(n, exp=2):` |
| `f(x, key=val)` | Pass keyword argument | `send(to="a", body="hi")` |
| `lambda x: expr` | Anonymous one-line function | `lambda x: x * 2` |
| `sorted(lst, key=fn)` | Sort using a key function | `sorted(lst, key=lambda x: x[1])` |
| `min(lst, key=fn)` | Minimum using a key function | `min(items, key=lambda i: i["price"])` |

---

## Task list

1. The flexible order totaler
2. The configurable report printer
3. The product sorter
4. The smart greeting system
5. The event logger

