# L32 Tasks — Practice: Advanced Topics

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The concurrent data processor (main project)

**Scenario**
A data engineering team needs a pipeline that fetches records from multiple mock APIs concurrently, processes them through a plugin-based system, caches expensive operations, and reports memory and timing statistics.

**Your task**
- Build the full system as described in `lesson.md`
- All advanced topics from L29–L31 must be demonstrably applied
- The pipeline must be measurably faster than the sequential equivalent
- Output must include a performance summary

**Expected output**
```
=== Concurrent Data Processor ===

Fetching 10 endpoints...
[RateLimiter] Max 5 req/s enforced
Fetched 10 endpoints in 2.04s (vs 12.5s sequential)

Registered processors: ['JSONProcessor', 'CSVProcessor', 'FilterProcessor']

Processing pipeline...
Records processed: 847
Cache hit rate: 73.2%
Peak memory: 4.2 MB

Results saved to results.json ✓

=== Profile Summary (top 3) ===
transform_record:  0.342s (34.1%)
parse_response:    0.218s (21.8%)
filter_records:    0.089s  (8.9%)
```

**File:** `main.py` (+ supporting modules)

---

## Task 2 — The performance audit tool

**Scenario**
A backend developer writes a standalone benchmarking script that tests four different approaches to a common data processing task, profiles each, and produces a comparison report with Big O analysis.

**Your task**
- Define a realistic task: find all customers who spent more than 10,000 USD total across a list of 50,000 transaction dicts
- Implement 4 approaches:
  - Approach A: nested loop (O(n²))
  - Approach B: `for` loop with `dict.get()` accumulation (O(n))
  - Approach C: `defaultdict` + single pass (O(n))
  - Approach D: generator pipeline + `groupby`-style dict comprehension (O(n))
- Profile all 4, measure memory with `tracemalloc`
- Print a final benchmark report

**Expected output**
```
=== Performance Audit: High-Value Customer Finder ===
n = 50,000 transactions

Approach A (nested):       8.420s  | Peak: 12.4 MB | O(n²)
Approach B (loop+dict):    0.048s  | Peak:  3.2 MB | O(n)
Approach C (defaultdict):  0.041s  | Peak:  3.1 MB | O(n)
Approach D (generator):    0.038s  | Peak:  1.8 MB | O(n) lazy

Recommendation: Approach D — fastest and most memory-efficient.
High-value customers found: 1,247
```

**File:** `task_02.py`

