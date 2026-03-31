# L31 Tasks — Performance & Memory

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The profile-guided optimizer

**Scenario**
A data analytics tool processes large lists of transactions. The developer suspects it is slow but doesn't know where. They use `cProfile` to find the bottleneck, then fix it.

**Your task**
- Write 3 versions of the same operation: find all unique transaction amounts above a threshold from a list of 500,000 random integers
  - Version A: nested loop with `if` (O(n²) simulation via repeated list scanning)
  - Version B: `for` loop with a set
  - Version C: set comprehension
- Profile all 3 versions using `cProfile.run()` or `time.perf_counter()`
- Print a comparison table showing execution time for each version
- Add a comment explaining which Big O class each version belongs to

**Expected output**
```
=== Performance Comparison (n=500,000) ===
Version A (nested):        4.820s  O(n²)
Version B (loop+set):      0.043s  O(n)
Version C (set comprehension): 0.031s  O(n)

Winner: Version C — 155x faster than Version A
```

**File:** `task_01.py`

---

## Task 2 — The slotted data model

**Scenario**
A geospatial service processes millions of GPS coordinate readings per day. The engineer needs to prove to their team that `__slots__` makes a significant memory difference at this scale.

**Your task**
- Create `RegularCoordinate` (normal class) and `SlottedCoordinate` (with `__slots__`) — both store `lat`, `lon`, `altitude`, `timestamp`
- Create 1,000,000 instances of each using list comprehensions
- Use `sys.getsizeof` on individual instances and `tracemalloc` to measure total memory for both collections
- Print a memory comparison report
- Also show that `SlottedCoordinate` raises `AttributeError` when you try to add an undeclared attribute

**Expected output**
```
=== Single Instance ===
Regular:  __dict__ size: 232 bytes
Slotted:  object size:    56 bytes
Saving:   75.9% per instance

=== 1,000,000 Instances ===
Regular collection:  ~342 MB
Slotted collection:  ~ 56 MB
Memory saved:        ~286 MB

Attribute guard test:
AttributeError: 'SlottedCoordinate' object has no attribute 'speed'
```

**File:** `task_02.py`

---

## Task 3 — The memoized calculator

**Scenario**
A financial modelling tool calculates compound interest projections for many different scenarios. The same base calculations are requested repeatedly with the same inputs. Caching eliminates redundant computation.

**Your task**
- Write `compound_interest(principal, rate, years)` — without cache, simulate expensive calculation with `time.sleep(0.01)`
- Apply `@lru_cache` to a second version
- Run 20 calculations: 10 unique sets of parameters + 10 repeats of the same
- Measure and compare total time for both versions
- Print `cache_info()` to show hits vs misses

**Expected output**
```
=== Without Cache ===
20 calculations completed in 0.204s

=== With lru_cache ===
20 calculations completed in 0.103s
Cache info: CacheInfo(hits=10, misses=10, maxsize=128, currsize=10)
Speedup: 1.98x (half the work done from cache)
```

**File:** `task_03.py`

---

## Task 4 — The Big O comparator

**Scenario**
A computer science lecturer needs a demonstration script showing how execution time grows with input size for different algorithmic complexities. Students will see O(1), O(n), O(n log n), and O(n²) side by side.

**Your task**
- Implement 4 functions, each representing a different Big O class:
  - `constant_lookup(data, key)` — dict lookup: O(1)
  - `linear_search(data, target)` — list scan: O(n)
  - `sort_and_search(data, target)` — sort then binary search: O(n log n)
  - `find_pair_slow(data, target_sum)` — nested loop pair finder: O(n²)
- Run each with input sizes: 1000, 5000, 10000, 50000
- Measure time for each combination and print a formatted table
- Show how the ratios between sizes grow differently for each complexity class

**Expected output**
```
Algorithm        n=1k     n=5k     n=10k    n=50k
O(1) lookup      0.00ms   0.00ms   0.00ms   0.00ms
O(n) search      0.05ms   0.25ms   0.50ms   2.48ms
O(n log n) sort  0.18ms   1.01ms   2.20ms   12.4ms
O(n²) pairs     12.30ms  305ms    1230ms   30200ms
```

**File:** `task_04.py`

---

## Task 5 — The memory-efficient data pipeline

**Scenario**
A log analysis tool processes a 100MB server log file. Loading the whole file into memory would crash on low-RAM machines. The tool must use generators throughout the entire pipeline.

**Your task**
- Create a large mock log file `server_logs.txt` with 100,000 lines programmatically (use a loop to write varied log lines: INFO, WARNING, ERROR with timestamps)
- Write a generator pipeline — every step must be a generator function or expression:
  - `read_lines(filepath)` — yields one line at a time
  - `parse_line(lines)` — yields parsed dicts `{level, timestamp, message}`
  - `filter_errors(records)` — yields only ERROR records
  - `format_report(records)` — yields formatted report lines
- Run the pipeline and write output to `error_report.txt`
- Use `tracemalloc` to show peak memory never exceeds a small threshold despite the large file

**Expected output**
```
Processing 100,000 log lines...
Errors found: 1,247
Report saved to error_report.txt

Peak memory used: 1.8 MB  (vs ~85 MB if loaded as a list)
```

**File:** `task_05.py`

