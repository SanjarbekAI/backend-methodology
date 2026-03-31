# L15 — Decorators & Generators

## Why this matters
Decorators let you add behaviour to functions without modifying their code — the backbone of logging, authentication, and caching in every Python framework. Generators let you process millions of records without loading them all into memory at once. Both are essential for professional Python.

---

## Topics

## `@decorator` syntax — Wrapping functions
A **decorator** is a function that takes another function as input, wraps it with extra behaviour, and returns the wrapped version. The `@` syntax is syntactic sugar for this pattern.

```python
def shout(func):                        # decorator function receives another function
    def wrapper(*args, **kwargs):       # wrapper runs before/after the original
        print("CALLING FUNCTION!")
        result = func(*args, **kwargs)  # call the original function
        print("DONE!")
        return result
    return wrapper                      # return the wrapper, not the result

@shout                                  # apply the decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Layla")
# CALLING FUNCTION!
# Hello, Layla!
# DONE!
```

**Without the `@` sugar, this is equivalent to:**
```python
greet = shout(greet)
```

> ⚠️ **Common mistake:** Forgetting `*args, **kwargs` in the wrapper. Without them, the decorator will break any function that takes arguments. Always include both in wrappers.

---

## Writing custom decorators — Real patterns
```python
import time
import functools

# Timing decorator — measures how long a function takes
def timer(func):
    @functools.wraps(func)          # preserves the original function's name and docstring
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

# Logging decorator — logs every call
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@timer
@log_call                          # multiple decorators — applied bottom up
def calculate_area(length, width):
    return length * width

calculate_area(5, 3)
```

> ⚠️ **Common mistake:** Not using `@functools.wraps(func)`. Without it, your decorated function loses its `__name__` and `__doc__`. This breaks debugging tools and documentation generators.

---

## `yield` — Pausing a function and producing values
A **generator function** uses `yield` instead of `return`. Each time `yield` is hit, the function pauses and hands back a value. The function's state is saved and continues from where it left off on the next call.

```python
def countdown(start):
    while start > 0:
        yield start               # pause here, give value to caller
        start -= 1                # resume here next time

gen = countdown(5)
print(next(gen))    # 5  — starts the generator, runs to first yield
print(next(gen))    # 4  — resumes from where it paused
print(next(gen))    # 3

# More common: loop over a generator
for num in countdown(3):
    print(num)      # 3, 2, 1
```

---

## Generator functions — Memory-efficient sequences
Generators compute values **one at a time** and never store the full sequence in memory. Perfect for large datasets.

```python
# Without generator — stores all 1 million numbers in memory
def get_million():
    return [i for i in range(1_000_000)]    # allocates a full list

# With generator — generates one number at a time
def generate_million():
    for i in range(1_000_000):
        yield i                              # one value at a time, no list in memory

# Real use — reading a large file line by line
def read_log_file(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()             # yield one line at a time

for line in read_log_file("server.log"):  # processes millions of lines, low memory
    if "ERROR" in line:
        print(line)
```

---

## Generator expressions — One-line generators
Like list comprehensions, but with `()` instead of `[]`. They are lazy — they don't compute anything until you ask.

```python
# List comprehension — computes everything immediately
squares_list = [x ** 2 for x in range(1000000)]  # huge list in memory

# Generator expression — lazy, computes one at a time
squares_gen = (x ** 2 for x in range(1000000))   # no memory used yet

# Only compute what you actually need
print(next(squares_gen))   # 0
print(next(squares_gen))   # 1
print(next(squares_gen))   # 4

# Sum without materializing the list
total = sum(x ** 2 for x in range(1000))   # efficient!
```

> ⚠️ **Common mistake:** Trying to reuse an exhausted generator. Once a generator has yielded all its values, it is done. You cannot reset it — you must create a new one.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `def decorator(func):` | Define a decorator | `def log(func):` |
| `@decorator` | Apply decorator to function | `@log` above `def f():` |
| `@functools.wraps(func)` | Preserve wrapped function metadata | In wrapper definition |
| `yield value` | Pause generator, produce value | `yield x` |
| `next(gen)` | Get next value from generator | `next(my_gen)` |
| `for x in gen:` | Iterate over all yielded values | `for n in countdown(5):` |
| `(expr for x in lst)` | Generator expression (lazy) | `(x**2 for x in range(10))` |
| `sum(gen_expr)` | Sum using generator — memory-efficient | `sum(x for x in range(1000))` |

---

## Task list

1. The function logger decorator
2. The access control decorator
3. The infinite ID generator
4. The lazy data reader
5. The retry decorator

