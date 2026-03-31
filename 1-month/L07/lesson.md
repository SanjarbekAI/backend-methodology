# L07 — Lists & Tuples

## Why this matters
A single variable holds one value. But what about a shopping cart with 40 products, a class with 30 students, or a leaderboard with 1000 scores? Lists let you store and work with collections of data. They are the most-used data structure in Python.

---

## Topics

## List CRUD operations — Create, Read, Update, Delete
A **list** is an ordered, changeable collection of items. Items are stored between square brackets `[]` and separated by commas.

```python
products = ["laptop", "headphones", "mouse", "keyboard"]

# CREATE — add items
products.append("monitor")          # add to the end
products.insert(1, "webcam")        # insert at index 1
print(products)
# ["laptop", "webcam", "headphones", "mouse", "keyboard", "monitor"]

# READ — access items
print(products[0])       # "laptop" — first item (index 0)
print(products[-1])      # "monitor" — last item (negative index)
print(len(products))     # 6 — total number of items

# UPDATE — change an item
products[2] = "earbuds"  # replace item at index 2
print(products[2])       # "earbuds"

# DELETE — remove items
products.remove("mouse")     # remove by value (first occurrence)
deleted = products.pop(0)    # remove by index AND return the value
print(deleted)               # "laptop"
del products[1]              # delete by index (no return value)
print(products)
```

> ⚠️ **Common mistake:** Calling `.remove()` with a value that doesn't exist in the list. It raises a `ValueError`. Always check with `in` first: `if "mouse" in products: products.remove("mouse")`.

---

## List slicing — Extracting sublists
Just like strings, lists support slicing with `[start:stop:step]`.

```python
scores = [95, 88, 72, 61, 90, 55, 83]

print(scores[1:4])     # [88, 72, 61] — items at index 1, 2, 3
print(scores[:3])      # [95, 88, 72] — first 3 items
print(scores[4:])      # [90, 55, 83] — from index 4 to end
print(scores[::2])     # [95, 72, 90, 83] — every second item
print(scores[::-1])    # [83, 55, 90, 61, 72, 88, 95] — reversed

# Useful list methods
print(sorted(scores))       # [55, 61, 72, 83, 88, 90, 95] — new sorted list
scores.sort()               # sorts in-place (modifies the original)
scores.reverse()            # reverses in-place
print(scores.index(88))     # finds the index of value 88
print(scores.count(95))     # counts how many times 95 appears
```

> ⚠️ **Common mistake:** Confusing `sorted(lst)` (returns new sorted list, original unchanged) with `lst.sort()` (modifies original, returns None). If you write `lst = lst.sort()`, you get `None`.

---

## Indexing — Accessing elements precisely
Every item in a list has two indexes: a positive one (from the front) and a negative one (from the back).

```python
team = ["Alice", "Bob", "Carol", "David", "Eve"]
#        0        1       2        3         4     ← positive index
#       -5       -4      -3       -2        -1     ← negative index

print(team[0])    # "Alice"
print(team[-1])   # "Eve"
print(team[-2])   # "David"

# Checking membership
print("Bob" in team)       # True
print("Frank" in team)     # False
print("Frank" not in team) # True
```

> ⚠️ **Common mistake:** Accessing an index that doesn't exist — e.g., `team[10]` on a 5-item list. This raises an `IndexError`. Always check `len()` or use `in` before accessing by index.

---

## Tuples — Immutable lists
A **tuple** is like a list but **immutable** — once created, you cannot change it. Tuples use parentheses `()`.

```python
# Creating a tuple
coordinates = (40.7128, -74.0060)   # latitude, longitude of New York
rgb = (255, 128, 0)                 # orange color
single = (42,)                      # single-item tuple — comma is required!

# Accessing — same as lists
print(coordinates[0])   # 40.7128
print(rgb[-1])          # 0

# Tuples are immutable — this raises a TypeError
# coordinates[0] = 0.0  ← cannot do this!

# Tuple unpacking — elegant assignment
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# Useful with functions that return multiple values
def get_dimensions():
    return 1920, 1080      # Python automatically packs these into a tuple

width, height = get_dimensions()
print(f"Screen: {width}x{height}")
```

> ⚠️ **Common mistake:** Forgetting the trailing comma for a single-item tuple. `(42)` is just the integer `42` in parentheses. `(42,)` is a tuple containing 42.

---

## Immutability — Why tuples exist
Use a **tuple** when the data should never change: coordinates, color codes, days of the week, configuration values. Use a **list** when the collection needs to grow, shrink, or change.

```python
# Good uses for tuples — fixed data
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
HTTP_SUCCESS_CODES = (200, 201, 202, 204)

# Good uses for lists — changing data
shopping_cart = ["bread", "milk"]
shopping_cart.append("eggs")        # cart changes — list is correct here
```

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `lst = [a, b, c]` | Create a list | `prices = [10, 20, 30]` |
| `lst[i]` | Access item at index i | `lst[0]` → first item |
| `lst[-1]` | Last item | `lst[-1]` |
| `lst[a:b]` | Slice from a to b (b excluded) | `lst[1:3]` |
| `lst.append(x)` | Add x to the end | `lst.append(5)` |
| `lst.insert(i, x)` | Insert x at index i | `lst.insert(0, "a")` |
| `lst.remove(x)` | Remove first occurrence of x | `lst.remove("a")` |
| `lst.pop(i)` | Remove & return item at index i | `lst.pop()` → last |
| `lst.sort()` | Sort in place | `lst.sort()` |
| `sorted(lst)` | Return new sorted list | `sorted([3,1,2])` |
| `len(lst)` | Number of items | `len(lst)` |
| `x in lst` | Check membership | `"a" in lst` |
| `tup = (a, b)` | Create a tuple | `point = (3, 4)` |
| `a, b = tup` | Unpack a tuple | `x, y = (1, 2)` |

---

## Task list

1. The shopping cart manager
2. The class gradebook
3. The top-3 extractor
4. The coordinates logger
5. The inventory restacker
6. The leaderboard system

