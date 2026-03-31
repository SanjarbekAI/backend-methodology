# L27 LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Design Underground System

- **Link:** https://leetcode.com/problems/design-underground-system/
- **Difficulty:** 🟡 Medium
- **Why this lesson:** SRP in action — separate the responsibility of tracking check-ins, recording journey completions, and calculating averages. Each responsibility maps cleanly to distinct data structures and methods.
- **Hint:** You need two dictionaries: one for in-progress journeys (keyed by customer ID) and one for completed route statistics. Think about what to store in each.
- **Your file:** `leetcode_1.py`

---

## Problem 2 — Insert Delete GetRandom O(1)

- **Link:** https://leetcode.com/problems/insert-delete-getrandom-o1/
- **Difficulty:** 🟡 Medium
- **Why this lesson:** ISP and SRP together — the class has three clearly-scoped operations, each with a single responsibility and no overlap. Designing clean method contracts before thinking about implementation is the SOLID approach.
- **Hint:** Getting a random element in O(1) requires array access. But deletion in O(1) requires a hash map. Think about how to combine both and keep them in sync.
- **Your file:** `leetcode_2.py`

