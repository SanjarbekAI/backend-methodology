# L32 LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Task Scheduler

- **Link:** https://leetcode.com/problems/task-scheduler/
- **Difficulty:** 🟡 Medium
- **Why this lesson:** Directly models CPU concurrency scheduling — the same problem your `asyncio` event loop solves when deciding which coroutine to run next and how long to wait between bursts.
- **Hint:** Think about the most frequent task — it determines the minimum time frame. The idle slots exist only to respect the cooldown period between identical tasks.
- **Your file:** `leetcode_1.py`

---

## Problem 2 — Sliding Window Maximum

- **Link:** https://leetcode.com/problems/sliding-window-maximum/
- **Difficulty:** 🔴 Hard
- **Why this lesson:** The naive O(n²) approach uses nested loops. The optimal O(n) approach uses a deque — demonstrating the same type of algorithmic improvement you practiced in the performance tasks. Profile thinking applied to algorithm selection.
- **Hint:** A monotonic deque (decreasing from front to back) lets you find the maximum in O(1) by always keeping the current window's maximum at the front.
- **Your file:** `leetcode_2.py`

