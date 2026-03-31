# L31 — Performance & Memory

## Why this matters
Code that works is not always code that scales. When your application processes millions of records, serves thousands of concurrent users, or runs on constrained hardware, performance and memory efficiency become business-critical. These tools help you find bottlenecks and eliminate them.

---

## Topics

## Profiling with `cProfile` — Finding the bottleneck
Never optimize without measuring first. `cProfile` shows you exactly which functions take the most time.

```python
import cProfile
import pstats
import io

def slow_function():
    result = []
    for i in range(100000):
        result.append(i ** 2)     # list append in a loop
    return result

def fast_function():
    return [i ** 2 for i in range(100000)]    # list comprehension

# Profile a function
profiler = cProfile.Profile()
profiler.enable()
slow_function()
profiler.disable()

stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
stats.print_stats(5)      # top 5 time-consuming calls
print(stream.getvalue())

# Quick one-liner profiling
cProfile.run("slow_function()", sort="cumulative")
```

> ⚠️ **Common mistake:** Optimizing code before profiling. You will almost always optimize the wrong part. Profile first, then optimize only the measured bottleneck.

---

## `__slots__` — Reducing memory per instance
By default, each Python instance stores its attributes in a `__dict__` (a dictionary). `__slots__` replaces this with a fixed-size structure, saving significant memory when you have millions of objects.

```python
import sys

class RegularPoint:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ("x", "y")           # declare allowed attributes

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

regular = RegularPoint(1.0, 2.0)
slotted = SlottedPoint(1.0, 2.0)

print(sys.getsizeof(regular.__dict__))  # ~232 bytes (the dict overhead)
print(sys.getsizeof(slotted))           # ~56 bytes (much smaller)

# SlottedPoint cannot have new attributes added at runtime
# slotted.z = 3.0  ← AttributeError — z is not in __slots__
```

**Memory impact at scale:**
```python
# 1 million regular points: ~350 MB
# 1 million slotted points:  ~56 MB
points_regular = [RegularPoint(i, i) for i in range(1_000_000)]
points_slotted = [SlottedPoint(i, i) for i in range(1_000_000)]
```

> ⚠️ **Common mistake:** Using `__slots__` in a class that needs to add arbitrary attributes dynamically, or in a class with a `__dict__`-using parent. `__slots__` only applies to the class that defines it.

---

## `functools.lru_cache` — Memoizing expensive computations
`lru_cache` stores the results of function calls. When called with the same arguments again, it returns the cached result instantly.

```python
from functools import lru_cache
import time

# Without cache — recalculates every time
def fib_slow(n: int) -> int:
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

# With cache — exponential → linear
@lru_cache(maxsize=None)    # maxsize=None means unlimited cache
def fib_fast(n: int) -> int:
    if n <= 1:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)

start = time.perf_counter()
print(fib_slow(35))     # slow
print(f"Slow: {time.perf_counter() - start:.3f}s")

start = time.perf_counter()
print(fib_fast(35))     # fast
print(f"Fast: {time.perf_counter() - start:.6f}s")

# Inspect cache stats
print(fib_fast.cache_info())
# CacheInfo(hits=33, misses=36, maxsize=None, currsize=36)

# Clear cache if needed
fib_fast.cache_clear()
```

> ⚠️ **Common mistake:** Using `lru_cache` on methods that use `self`. The default `lru_cache` treats `self` as a cache key, which prevents the object from being garbage collected (memory leak). Use `functools.cached_property` for computed properties, or be careful with class methods.

---

## Big O basics — Understanding algorithmic complexity
**Big O notation** describes how an algorithm's time or space requirements grow with input size `n`.

```python
# O(1) — constant time: same speed regardless of input size
def get_first(lst: list) -> int:
    return lst[0]

# O(n) — linear time: speed grows proportionally with input
def find_max(lst: list) -> int:
    maximum = lst[0]
    for x in lst:                # one pass through the list
        if x > maximum:
            maximum = x
    return maximum

# O(n²) — quadratic time: nested loops — slow on large inputs
def has_duplicate_slow(lst: list) -> bool:
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):   # nested loop
            if lst[i] == lst[j]:
                return True
    return False

# O(n) — using a set (hash lookup is O(1))
def has_duplicate_fast(lst: list) -> bool:
    seen = set()
    for x in lst:
        if x in seen:        # O(1) lookup
            return True
        seen.add(x)
    return False
```

| Big O | Name | Example |
|---|---|---|
| O(1) | Constant | Dict/set lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | List scan |
| O(n log n) | Log-linear | `sorted()` |
| O(n²) | Quadratic | Nested loops |

---

## Memory-efficient patterns
```python
# Use generators instead of lists for large data
total = sum(x ** 2 for x in range(10_000_000))  # generator: uses ~100 bytes
# vs [x**2 for x in range(10_000_000)]            # list: uses ~400 MB

# Use tuple instead of list for immutable sequences
WEEKDAYS = ("Mon", "Tue", "Wed", "Thu", "Fri")   # tuple: ~200 bytes
# vs WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]  # list: ~280 bytes

# Use numpy-style approach for numeric bulk processing (stdlib)
from array import array
int_array = array("i", range(1_000_000))   # typed array: ~4 MB vs ~35 MB for list
```

---

## Quick reference

| Tool | What it does | When to use |
|---|---|---|
| `cProfile.run("code()")` | Profile code, show timing | First step before any optimization |
| `__slots__ = (...)` | Fixed attributes, less memory | Many instances (10k+) of one class |
| `@lru_cache(maxsize=N)` | Cache function results | Pure functions with repeated calls |
| `lru_cache.cache_info()` | See cache hits/misses | After caching — verify it's helping |
| Generator expression | Lazy evaluation, no list | Large sequences you don't need all at once |
| `sys.getsizeof(obj)` | Memory size of object | Benchmarking memory usage |

---

## Task list

1. The profile-guided optimizer
2. The slotted data model
3. The memoized calculator
4. The Big O comparator
5. The memory-efficient data pipeline

## LeetCode

- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — 🟡 Medium — Choosing the right data structure (bucket sort or heap) versus the naive O(n log n) sort directly demonstrates Big O tradeoffs.
- [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) — 🔴 Hard — A performance-critical design problem where O(n) vs O(log n) per operation is the entire challenge.

