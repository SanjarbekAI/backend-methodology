# L29 Tasks — Concurrency: Threading & Async

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The parallel file downloader

**Scenario**
A data pipeline tool downloads multiple large report files from remote servers. Running downloads sequentially takes too long — the team needs them to run in parallel using threads.

**Your task**
- Import `threading` and `time`
- Define a `simulate_download(filename: str, size_mb: float)` function that sleeps for `size_mb * 0.3` seconds (simulating download time) and prints start/end messages
- Run 5 "downloads" sequentially first, measure total time with `time.time()`
- Then run the same 5 downloads using threads, measure total time again
- Print both times and the speedup ratio

**Expected output**
```
=== Sequential ===
Downloading report_q1.pdf (12.0 MB)...
Downloading data_export.csv (8.5 MB)...
...
Sequential time: 14.25s

=== Threaded ===
Downloading report_q1.pdf (12.0 MB)...
Downloading data_export.csv (8.5 MB)...
...
Threaded time: 3.60s
Speedup: 3.96x
```

**File:** `task_01.py`

---

## Task 2 — The thread-safe counter

**Scenario**
A web analytics system counts page views from multiple concurrent user sessions. Without thread safety, the count is corrupted. The team must implement a thread-safe counter class.

**Your task**
- Create a `PageViewCounter` class with a private `_count: int` and a `threading.Lock`
- Methods: `increment()`, `get_count() -> int`, `reset()`
- First demonstrate the race condition: run 5 threads each incrementing 10,000 times WITHOUT a lock, print the incorrect result
- Then run the same test WITH the lock, show the correct result (50,000)

**Expected output**
```
=== Without Lock (race condition) ===
Expected: 50000 | Got: 47832  ← corrupted!

=== With Lock (thread-safe) ===
Expected: 50000 | Got: 50000  ✓
```

**File:** `task_02.py`

---

## Task 3 — The async API fetcher

**Scenario**
A backend aggregator service fetches data from 5 different microservice endpoints before building a dashboard response. Running them sequentially adds latency — they must run concurrently with `asyncio`.

**Your task**
- Import `asyncio`
- Write `async def fetch_service(name: str, delay: float) -> dict` that simulates a service call with `asyncio.sleep(delay)` and returns `{"service": name, "status": "ok", "data": "..."}`
- Define 5 services with different simulated response times
- Run them sequentially and measure time
- Run them concurrently with `asyncio.gather()` and measure time
- Print each result and both total times

**Expected output**
```
=== Sequential ===
users: ok (2.0s)
orders: ok (1.5s)
...
Total: 8.5s

=== Concurrent ===
users: ok
orders: ok
...
Total: 2.0s  ← limited by the slowest service
```

**File:** `task_03.py`

---

## Task 4 — The concurrent order processor

**Scenario**
An e-commerce platform processes orders in a background worker. Each order goes through validation, inventory check, and payment — each step simulated as an async operation.

**Your task**
- Write `async def validate_order(order_id: str) -> bool` (0.3s delay)
- Write `async def check_inventory(order_id: str) -> bool` (0.5s delay)
- Write `async def process_payment(order_id: str, amount: float) -> str` (1.0s delay)
- Write `async def fulfill_order(order_id: str, amount: float) -> dict` that runs all 3 sequentially for one order (they depend on each other)
- Write `async def process_batch(orders: list[dict]) -> None` that processes all orders concurrently using `asyncio.gather()`
- Process a batch of 5 orders and print results

**Expected output**
```
Processing batch of 5 orders...
ORD-001: validated ✓ | inventory ✓ | payment TXN-8842 ✓
ORD-002: validated ✓ | inventory ✓ | payment TXN-8843 ✓
...
Batch complete in 1.82s (vs 9.0s sequential)
```

**File:** `task_04.py`

---

## Task 5 — The background task scheduler

**Scenario**
A server monitoring tool runs periodic health checks in background threads while the main program continues running. Each check runs on its own schedule without blocking the others.

**Your task**
- Import `threading` and `time`
- Write `run_check(name: str, interval: float, runs: int)` that runs `runs` times, sleeping `interval` seconds between each
- Create 3 monitoring tasks with different intervals: CPU check (1s), Memory check (2s), Disk check (3s)
- Run all 3 as daemon threads (set `daemon=True`) so they stop when the main program exits
- Let the main program run for 7 seconds (sleep), then print "Main program done." and exit

**Expected output**
```
[CPU Check] Running... (1/3) at 0.00s
[Memory Check] Running... (1/2) at 0.00s
[Disk Check] Running... (1/1) at 0.00s
[CPU Check] Running... (2/3) at 1.00s
[Memory Check] Running... (2/2) at 2.00s
[CPU Check] Running... (3/3) at 2.00s
...
Main program done.
```

**File:** `task_05.py`

