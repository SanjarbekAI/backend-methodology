# L12 — Functions: Basics & Scope

## Why this matters
Copy-pasting the same block of code five times is not programming — it's a maintenance nightmare. Functions let you write a piece of logic once and reuse it everywhere. They are the first step from writing scripts to building real software.

---

## Topics

## `def` and `return` — Defining and calling functions
A function is a named, reusable block of code. Define it once with `def`, then call it as many times as you need.

```python
# Define the function
def greet_user(name):           # 'name' is a parameter
    message = f"Hello, {name}! Welcome."
    return message              # send the result back to the caller

# Call the function
result = greet_user("Layla")   # "Layla" is the argument
print(result)                  # Hello, Layla! Welcome.

# Call it again with different input
print(greet_user("Rustam"))    # Hello, Rustam! Welcome.
```

**Real example — discount calculator:**
```python
def calculate_total(price, discount_percent):
    discount = price * (discount_percent / 100)
    final = price - discount
    return final

print(calculate_total(500000, 10))   # 450000.0
print(calculate_total(200000, 25))   # 150000.0
```

> ⚠️ **Common mistake:** Forgetting `return`. A function without `return` implicitly returns `None`. If you do `total = calculate_total(...)` and forget `return`, `total` will be `None`.

---

## Parameters — The inputs a function expects
**Parameters** are variables listed in the function definition. **Arguments** are the actual values you pass when calling the function.

```python
def register_student(name, age, faculty):    # 3 parameters
    print(f"Registered: {name}, {age}, {faculty}")

register_student("Kamola", 20, "CS")         # 3 arguments — positional
register_student(age=21, name="Bobur", faculty="Math")  # keyword arguments — order doesn't matter
```

**Returning multiple values:**
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)       # Python packs these into a tuple

low, high = get_min_max([88, 72, 95, 61])  # tuple unpacking
print(f"Min: {low}, Max: {high}")           # Min: 61, Max: 95
```

> ⚠️ **Common mistake:** Calling a function with the wrong number of arguments. Python raises a `TypeError` immediately. Count your parameters vs arguments.

---

## Local vs global scope — Where variables live
**Scope** determines where a variable can be seen and used. Variables defined inside a function are **local** — they only exist during that function call. Variables defined at the top level are **global**.

```python
company_name = "TechCorp"       # global variable — visible everywhere

def show_info():
    employee = "Rustam"         # local variable — only visible inside this function
    print(f"{employee} works at {company_name}")   # can read global from inside

show_info()                     # Rustam works at TechCorp
# print(employee)               # NameError! 'employee' doesn't exist out here
```

**Using `global` to modify a global variable (use sparingly):**
```python
counter = 0                     # global counter

def increment():
    global counter              # declare we mean the global one
    counter += 1                # now this modifies the global variable

increment()
increment()
print(counter)                  # 2
```

> ⚠️ **Common mistake:** Overusing `global`. Modifying global state inside functions makes code unpredictable and hard to test. Prefer passing values in and returning results out.

---

## `None` return — Functions that do, not give
Some functions perform an action (print, write to file, update something) and don't need to return a value. They implicitly return `None`.

```python
def log_event(event_name):
    with open("events.log", "a") as f:
        f.write(f"{event_name}\n")
    # no return statement — returns None automatically

result = log_event("user_login")
print(result)                    # None — that's fine, we didn't need a value
```

**Checking for None:**
```python
def find_user(user_id, database):
    for user in database:
        if user["id"] == user_id:
            return user          # found — return the user dict
    return None                  # not found

users = [{"id": 1, "name": "Ali"}, {"id": 2, "name": "Sara"}]
user = find_user(2, users)

if user is None:                 # always use 'is None', not '== None'
    print("User not found")
else:
    print(f"Found: {user['name']}")
```

> ⚠️ **Common mistake:** Comparing with `== None` instead of `is None`. While often equivalent, `is None` is the correct and Pythonic way to check for `None`.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `def name(params):` | Define a function | `def greet(name):` |
| `return value` | Send a value back to the caller | `return total` |
| `func(args)` | Call a function | `greet("Ali")` |
| `func(key=val)` | Call with keyword argument | `greet(name="Ali")` |
| `return a, b` | Return multiple values as tuple | `return min, max` |
| Local variable | Defined inside function, not visible outside | `def f(): x = 1` |
| Global variable | Defined outside, visible everywhere | `x = 1` at top level |
| `global x` | Modify a global inside a function | `global counter` |
| `return None` / no return | Function returns None | implicit |
| `x is None` | Check if x is None | `if result is None:` |

---

## Task list

1. The tax calculator
2. The BMI checker
3. The password strength tester
4. The invoice generator
5. The search function

