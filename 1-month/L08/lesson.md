# L08 — Sets & Dictionaries

## Why this matters
Lists store ordered sequences, but what if you need to look something up by name instead of position? What if you need to remove all duplicates in one step? Dictionaries and sets solve these problems — they are the backbone of every real data system, from user profiles to inventory tracking.

---

## Topics

## Set operations — Collections with no duplicates
A **set** is an unordered collection where every item is unique. Sets use curly braces `{}`.

```python
# Creating sets
visited_cities = {"Tashkent", "Samarkand", "Bukhara", "Tashkent"}  # duplicate is removed
print(visited_cities)   # {'Tashkent', 'Samarkand', 'Bukhara'} — order may vary

# Adding and removing
visited_cities.add("Namangan")          # add a single item
visited_cities.discard("Bukhara")       # remove if present (no error if missing)
visited_cities.remove("Samarkand")      # remove — raises KeyError if not found

# Membership check — very fast
print("Tashkent" in visited_cities)     # True

# Set math operations — great for comparing collections
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a | set_b)    # union:        {1, 2, 3, 4, 5, 6, 7, 8} — all items
print(set_a & set_b)    # intersection: {4, 5} — items in BOTH sets
print(set_a - set_b)    # difference:   {1, 2, 3} — in A but not in B
print(set_a ^ set_b)    # symmetric diff: {1, 2, 3, 6, 7, 8} — in one but not both
```

**Real use — removing duplicates from a list:**
```python
user_ids = [101, 202, 101, 303, 202, 404]
unique_ids = list(set(user_ids))         # convert to set (removes dupes), back to list
print(unique_ids)                         # [101, 202, 303, 404] — order not guaranteed
```

> ⚠️ **Common mistake:** Using `.remove()` on a set with an item that doesn't exist — it raises a `KeyError`. Use `.discard()` instead when you're not sure the item exists.

---

## Dictionary methods — Key-value storage
A **dictionary** stores data as **key: value** pairs. Think of it like a real dictionary: you look up a word (key) and find its definition (value). Keys must be unique.

```python
# Creating a dictionary
student = {
    "name": "Layla Karimova",
    "age": 21,
    "GPA": 3.8,
    "is_enrolled": True
}

# Accessing values
print(student["name"])              # "Layla Karimova"
print(student.get("age"))           # 21 — safer than [] (no KeyError if missing)
print(student.get("phone", "N/A"))  # "N/A" — default if key doesn't exist

# Adding and updating
student["email"] = "layla@uni.edu"  # add new key-value
student["age"] = 22                 # update existing value

# Deleting
del student["is_enrolled"]          # delete a key-value pair
popped = student.pop("GPA")         # remove and return the value

# Looping
for key in student:                         # loop over keys
    print(f"{key}: {student[key]}")

for key, value in student.items():          # loop over key-value pairs
    print(f"{key} → {value}")

# Useful methods
print(student.keys())    # dict_keys(['name', 'age', 'email'])
print(student.values())  # dict_values(['Layla Karimova', 22, 'layla@uni.edu'])
print(len(student))      # 3
print("name" in student) # True — checks keys
```

> ⚠️ **Common mistake:** Using `dict["key"]` when the key might not exist. This raises a `KeyError`. Always use `.get()` when the key's presence is uncertain.

---

## Nested dicts — Dictionaries inside dictionaries
Dictionary values can themselves be dictionaries. This lets you represent complex, real-world data structures.

```python
employees = {
    "E001": {
        "name": "Bobur Nazarov",
        "department": "Engineering",
        "salary": 8500000
    },
    "E002": {
        "name": "Sara Yusupova",
        "department": "Marketing",
        "salary": 6200000
    }
}

# Accessing nested data
print(employees["E001"]["name"])           # "Bobur Nazarov"
print(employees["E002"]["salary"])         # 6200000

# Updating nested data
employees["E001"]["salary"] = 9000000      # give Bobur a raise

# Looping through nested data
for emp_id, info in employees.items():
    print(f"{emp_id}: {info['name']} — {info['department']}")
```

> ⚠️ **Common mistake:** Forgetting that when you modify a nested dict, you are modifying it in place. There is only one copy of the nested dict — changes are permanent.

---

## dict vs set — Knowing when to use which

| Feature | `set` | `dict` |
|---|---|---|
| Stores | Values only | Key-value pairs |
| Duplicates | Not allowed | Keys must be unique; values can repeat |
| Ordered | No (Python 3.7+ sets are unordered) | Yes (Python 3.7+ dicts maintain insertion order) |
| Access | `item in set` | `dict[key]` or `dict.get(key)` |
| Best for | Membership checks, deduplication | Lookups, structured data |

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `s = {a, b, c}` | Create a set | `s = {1, 2, 3}` |
| `s.add(x)` | Add item to set | `s.add(4)` |
| `s.discard(x)` | Remove if present (safe) | `s.discard(99)` |
| `A \| B` | Union (all items) | `{1,2} \| {2,3}` → `{1,2,3}` |
| `A & B` | Intersection (common) | `{1,2} & {2,3}` → `{2}` |
| `A - B` | Difference (in A not B) | `{1,2} - {2,3}` → `{1}` |
| `d = {k: v}` | Create dictionary | `d = {"a": 1}` |
| `d[key]` | Access value by key | `d["a"]` → `1` |
| `d.get(key, default)` | Safe access with fallback | `d.get("b", 0)` |
| `d[key] = val` | Add or update key | `d["b"] = 2` |
| `del d[key]` | Delete a key | `del d["a"]` |
| `d.keys()` | All keys | `d.keys()` |
| `d.values()` | All values | `d.values()` |
| `d.items()` | All key-value pairs | `for k, v in d.items()` |

---

## Task list

1. The duplicate cleaner
2. The student registry
3. The product catalog lookup
4. The permission checker
5. The nested employee database
6. The word frequency counter

