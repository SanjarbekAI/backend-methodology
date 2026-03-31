# L29 LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Print in Order

- **Link:** https://leetcode.com/problems/print-in-order/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** A direct threading synchronization exercise — three methods must execute in order across different threads. Apply what you learned about locks and threading events to guarantee sequence.
- **Hint:** Consider using `threading.Event` or semaphores to signal between threads. A thread should wait until it receives the "go" signal before printing.
- **Your file:** `leetcode_1.py`

---

## Problem 2 — Web Crawler Multithreaded

- **Link:** https://leetcode.com/problems/web-crawler-multithreaded/
- **Difficulty:** 🟡 Medium
- **Why this lesson:** Applies threading to a real-world I/O-bound task — fetching URLs concurrently while using a lock to protect the shared "visited" set from race conditions.
- **Hint:** Use a thread pool (`concurrent.futures.ThreadPoolExecutor`) for clean thread management. The lock must protect the visited URLs set, not the HTTP fetch itself.
- **Your file:** `leetcode_2.py`

