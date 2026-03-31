# L29 — Concurrency: Threading & Async

## Why this matters
A server that handles one request at a time is useless in production. Threading and async let your programs do multiple things concurrently — download files while processing data, handle thousands of web requests simultaneously, and run background jobs without blocking the user.

---

## Topics

## `threading` module — Running code in parallel threads
A **thread** is a separate stream of execution within the same process. Use threads for I/O-bound tasks (network, file, database).

```python
import threading
import time

def download_file(filename: str, duration: float) -> None:
    print(f"Starting download: {filename}")
    time.sleep(duration)                          # simulate network delay
    print(f"Finished: {filename}")

# Without threads — sequential (slow)
# Total time: 3 + 2 + 1 = 6 seconds
download_file("report.pdf", 3)
download_file("image.jpg", 2)
download_file("data.csv", 1)

# With threads — concurrent (fast)
# Total time: ~3 seconds (longest task)
t1 = threading.Thread(target=download_file, args=("report.pdf", 3))
t2 = threading.Thread(target=download_file, args=("image.jpg", 2))
t3 = threading.Thread(target=download_file, args=("data.csv", 1))

t1.start()    # start all three
t2.start()
t3.start()

t1.join()     # wait for all to finish before continuing
t2.join()
t3.join()
print("All downloads complete.")
```

> ⚠️ **Common mistake:** Not calling `.join()`. Without it, the main program may exit before the threads finish, cutting them off mid-execution.

---

## `Lock` — Preventing race conditions
A **race condition** occurs when two threads access shared data simultaneously, producing unpredictable results.

```python
import threading

counter = 0
lock = threading.Lock()            # a mutual-exclusion lock

def increment_safe() -> None:
    global counter
    for _ in range(100000):
        with lock:                 # only one thread enters this block at a time
            counter += 1

t1 = threading.Thread(target=increment_safe)
t2 = threading.Thread(target=increment_safe)
t1.start(); t2.start()
t1.join(); t2.join()
print(counter)    # Always 200000 — safe!

# Without lock: counter might be 187432 or 193801 — unpredictable
```

> ⚠️ **Common mistake:** Holding a lock for too long (inside slow I/O operations). Only lock around the minimum critical section — the shared variable update — not the entire operation.

---

## `asyncio` — Cooperative multitasking
`asyncio` is Python's built-in async framework. Unlike threads, `async/await` is single-threaded and cooperative — tasks yield control to each other at `await` points. Ideal for high-volume I/O (web servers, APIs).

```python
import asyncio

async def fetch_data(url: str, delay: float) -> str:
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)           # yield control during the wait
    return f"Data from {url}"

async def main() -> None:
    # Run all three concurrently
    results = await asyncio.gather(
        fetch_data("api/users", 2),
        fetch_data("api/orders", 1),
        fetch_data("api/products", 3),
    )
    for result in results:
        print(result)

asyncio.run(main())    # the entry point for async code
```

**Output** (total ~3 seconds, not 6):
```
Fetching api/users...
Fetching api/orders...
Fetching api/products...
Data from api/users
Data from api/orders
Data from api/products
```

> ⚠️ **Common mistake:** Calling `asyncio.run()` inside an already-running event loop (e.g., in Jupyter notebooks). Use `await main()` instead, or `asyncio.get_event_loop().run_until_complete(main())`.

---

## `async/await` and coroutines
An `async def` function is a **coroutine** — it can be paused and resumed. You must `await` a coroutine to actually run it.

```python
import asyncio

async def process_order(order_id: int) -> dict:
    print(f"Processing order {order_id}...")
    await asyncio.sleep(0.5)               # simulate DB/API call
    return {"id": order_id, "status": "confirmed"}

async def run_orders() -> None:
    # Sequential — slow (each waits for the previous)
    # result1 = await process_order(1)
    # result2 = await process_order(2)

    # Concurrent — fast (all run together)
    results = await asyncio.gather(
        *[process_order(i) for i in range(1, 6)]
    )
    for r in results:
        print(f"Order {r['id']}: {r['status']}")

asyncio.run(run_orders())
```

---

## Threading vs Async — Choosing the right tool

| Feature | `threading` | `asyncio` |
|---|---|---|
| Model | Preemptive (OS manages switching) | Cooperative (you manage switching with `await`) |
| Overhead | Higher (OS threads) | Lower (single-threaded) |
| Race conditions | Possible — need locks | Not possible (single thread) |
| Best for | I/O-bound with blocking libraries | I/O-bound with async-compatible libraries |
| Python GIL | Limited CPU parallelism | Not affected (single thread) |

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `threading.Thread(target=fn, args=(...))` | Create a thread | `t = Thread(target=worker)` |
| `t.start()` | Start the thread | `t.start()` |
| `t.join()` | Wait for thread to finish | `t.join()` |
| `threading.Lock()` | Create a mutex lock | `lock = Lock()` |
| `with lock:` | Acquire and release lock safely | `with lock: counter += 1` |
| `async def fn():` | Define a coroutine | `async def fetch():` |
| `await expr` | Pause and wait for a coroutine | `await asyncio.sleep(1)` |
| `asyncio.run(coro)` | Run coroutine as program entry | `asyncio.run(main())` |
| `asyncio.gather(*coros)` | Run multiple coroutines concurrently | `await asyncio.gather(f1(), f2())` |
| `asyncio.sleep(n)` | Non-blocking sleep | `await asyncio.sleep(1)` |

---

## Task list

1. The parallel file downloader
2. The thread-safe counter
3. The async API fetcher
4. The concurrent order processor
5. The background task scheduler

## LeetCode

- [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) — 🟡 Medium — Directly applies threading to crawl multiple URLs concurrently while using a lock to protect the visited set.
- [Print in Order](https://leetcode.com/problems/print-in-order/) — 🟢 Easy — A threading synchronization problem where you must guarantee execution order across threads using locks or events.

