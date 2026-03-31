# L09 — User Input & Error Handling

## Why this matters
Every real program talks to users — and users make mistakes. They type letters where you expect numbers, leave fields blank, or enter values your program never anticipated. Error handling is what separates a professional application from one that crashes the moment something unexpected happens.

---

## Topics

## `input()` — Reading from the user
`input()` pauses the program and waits for the user to type something and press Enter. It **always returns a string**, regardless of what the user types.

```python
name = input("What is your name? ")   # shows prompt, waits for user
print(f"Hello, {name}!")              # uses whatever the user typed

city = input("Your city: ")
print(f"You live in {city}.")
```

> ⚠️ **Common mistake:** Forgetting that `input()` always returns a string. If the user types `25`, Python receives the string `"25"`, not the integer `25`. You cannot do math on it without converting it first.

---

## Type conversion of input — Making numbers usable
Because `input()` always returns a string, you must convert it to the correct type before doing anything numeric.

```python
# Wrong — this will crash or give wrong result
age = input("Enter your age: ")
# age is "25" (string), not 25 (int)
# print(age + 1)  ← TypeError: can only concatenate str to str

# Correct — cast immediately
age = int(input("Enter your age: "))      # now age is an integer
salary = float(input("Enter salary: "))   # salary is a float

next_year = age + 1
print(f"Next year you will be {next_year}.")
```

**What happens if the user types "abc" when you expect a number?**
It crashes with a `ValueError` — which is exactly why we need error handling.

> ⚠️ **Common mistake:** Casting inside `input()` without wrapping it in `try/except`. `int(input(...))` will crash if the user types anything non-numeric.

---

## `try`, `except` — Catching errors gracefully
A `try` block contains code that might fail. If it does, Python jumps to the `except` block instead of crashing.

```python
try:
    age = int(input("Enter your age: "))   # this might fail
    print(f"You are {age} years old.")
except ValueError:
    print("Error: Please enter a valid number.")

# If the user types "hello", the program prints the error message and continues
# If the user types "25", it works normally
```

**Multiple except blocks — handling different error types:**
```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 ÷ {number} = {result}")
except ValueError:
    print("That is not a valid number.")    # user typed text
except ZeroDivisionError:
    print("Cannot divide by zero!")         # user typed 0
```

> ⚠️ **Common mistake:** Using a bare `except:` (no error type) — it catches everything including keyboard interrupts and system exits. Always be specific about which exceptions you handle.

---

## `finally` — Code that always runs
The `finally` block runs **no matter what** — whether an error occurred or not. Use it for cleanup actions like closing files or releasing resources.

```python
try:
    file_name = input("Enter filename: ")
    f = open(file_name, "r")          # this might fail if file doesn't exist
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found. Check the name and try again.")
finally:
    print("Attempted to read file.")  # always runs, success or failure
```

---

## Common exceptions — The ones you will see most
```python
# ValueError — wrong value type
int("hello")                   # ValueError: invalid literal for int()

# TypeError — wrong operation for the type
"hello" + 5                    # TypeError: can only concatenate str (not "int") to str

# ZeroDivisionError — dividing by zero
10 / 0                         # ZeroDivisionError: division by zero

# IndexError — list index out of range
lst = [1, 2, 3]
print(lst[10])                 # IndexError: list index out of range

# KeyError — dict key doesn't exist
d = {"a": 1}
print(d["b"])                  # KeyError: 'b'

# FileNotFoundError — file doesn't exist
open("ghost.txt", "r")         # FileNotFoundError: No such file or directory
```

**Catching multiple exceptions at once:**
```python
try:
    value = int(input("Enter: "))
    print(10 / value)
except (ValueError, ZeroDivisionError) as e:
    print(f"Input error: {e}")    # e contains the error message
```

> ⚠️ **Common mistake:** Not knowing what exception to catch. Run the code first without `try/except`, see what error Python raises, then catch that specific exception by name.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `input("prompt")` | Read user input as string | `name = input("Name: ")` |
| `int(input(...))` | Read and cast to integer | `age = int(input("Age: "))` |
| `float(input(...))` | Read and cast to float | `price = float(input(...))` |
| `try: ... except E:` | Handle specific exception E | `except ValueError:` |
| `except (E1, E2):` | Handle multiple exceptions | `except (ValueError, TypeError):` |
| `except E as e:` | Capture error message in `e` | `except ValueError as e:` |
| `finally:` | Always runs after try/except | `finally: cleanup()` |
| `ValueError` | Wrong type/value | `int("abc")` |
| `TypeError` | Wrong type for operation | `"a" + 1` |
| `ZeroDivisionError` | Divide by zero | `5 / 0` |
| `IndexError` | List index out of range | `lst[99]` |
| `KeyError` | Dict key not found | `d["missing"]` |
| `FileNotFoundError` | File does not exist | `open("x.txt")` |

---

## Task list

1. The age registration form
2. The calculator with guard
3. The menu-driven app
4. The stock lookup tool
5. The safe list accessor
6. The robust data entry loop

