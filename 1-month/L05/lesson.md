# L05 — Booleans & if...else

## Why this matters
Every decision in a program — should the user be allowed to log in? Is the payment valid? Should we show the discount? — is powered by conditional logic. `if...else` is the heartbeat of any interactive program, and you will use it in every single project you ever build.

---

## Topics

## Boolean values — The language of decisions
Booleans are the simplest data type: just `True` or `False`. Every condition you write eventually evaluates to one of these two values.

```python
is_raining = True
has_umbrella = False

print(is_raining)           # True
print(not is_raining)       # False — flips the value

# These expressions all evaluate to True or False
print(10 > 5)               # True
print(10 == 5)              # False
print("admin" == "admin")   # True

# Truthiness — Python treats some values as True/False automatically
print(bool(0))       # False — zero is falsy
print(bool(""))      # False — empty string is falsy
print(bool(None))    # False — None is falsy
print(bool(42))      # True  — any non-zero number is truthy
print(bool("hello")) # True  — any non-empty string is truthy
```

> ⚠️ **Common mistake:** Confusing `bool(0)` with `bool("0")`. The number `0` is falsy. The string `"0"` is truthy (it's not empty).

---

## `if`, `elif`, `else` — Making decisions
The `if` statement runs a block of code only if the condition is `True`. Use `elif` for additional conditions, and `else` as the fallback.

```python
score = 72

if score >= 90:
    print("Grade: A")          # runs if score is 90 or above
elif score >= 75:
    print("Grade: B")          # runs if score is 75–89
elif score >= 60:
    print("Grade: C")          # runs if score is 60–74  ← this runs
else:
    print("Grade: F")          # runs if none of the above were True

# Output: Grade: C
```

**Real example — a login check:**
```python
username = "admin"
password = "secure123"
is_active = True

if username == "admin" and password == "secure123" and is_active:
    print("Login successful. Welcome!")
else:
    print("Login failed. Check your credentials.")
```

> ⚠️ **Common mistake:** Writing multiple `if` statements instead of `elif`. Each `if` is checked independently; `elif` only runs when the previous condition was False. Use `elif` when conditions are mutually exclusive.

---

## Nested conditions — Conditions inside conditions
You can place an `if` statement inside another `if` block. This is called **nesting**. Keep it to 2–3 levels maximum — deeper nesting is hard to read.

```python
is_member = True
cart_total = 85

if is_member:
    if cart_total >= 100:
        print("You get free shipping + member discount!")
    else:
        print("You get the member discount only.")
else:
    if cart_total >= 100:
        print("You get free shipping for orders over 100.")
    else:
        print("Standard pricing applies.")

# Output: You get the member discount only.
```

> ⚠️ **Common mistake:** Deep nesting that becomes unreadable. If you have more than 3 levels, consider restructuring with `and`/`or` or by using functions (learned in Month 2).

---

## `match` statement — Python's modern switch
The `match` statement (Python 3.10+) is a clean alternative to long `if/elif` chains when you are comparing one value against many specific options.

```python
day = "Monday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a workday.")          # matches weekdays
    case "Saturday" | "Sunday":
        print("It's the weekend!")        # matches weekend
    case _:
        print("Unknown day.")             # default (like else)

# Output: It's a workday.
```

**Another real example — HTTP status codes:**
```python
status_code = 404

match status_code:
    case 200:
        print("OK — request successful")
    case 201:
        print("Created — new resource added")
    case 404:
        print("Not Found — resource does not exist")   # this runs
    case 500:
        print("Server Error — something went wrong")
    case _:
        print("Unknown status code")
```

> ⚠️ **Common mistake:** Using `match` in Python versions below 3.10. If you need to support older Python, use `if/elif` instead.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `if condition:` | Run block if condition is True | `if age >= 18:` |
| `elif condition:` | Otherwise, check another condition | `elif age >= 13:` |
| `else:` | Fallback if no condition matched | `else: print("child")` |
| `and` | Both conditions must be True | `a > 0 and b > 0` |
| `or` | At least one must be True | `a == 0 or b == 0` |
| `not` | Flip True to False (or vice versa) | `not is_closed` |
| `bool(x)` | Convert x to True/False | `bool(0)` → `False` |
| `match value:` | Match against specific cases (3.10+) | `match status:` |
| `case x:` | One branch of match | `case 200:` |
| `case _:` | Default / fallback branch | `case _: ...` |
| `x if cond else y` | Inline (ternary) condition | `"yes" if ok else "no"` |

---

## Task list

1. The age gate
2. The grade classifier
3. The shipping calculator
4. The ATM access system
5. The status code responder
6. The loan eligibility checker

