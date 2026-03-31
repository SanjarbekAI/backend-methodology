# L24 LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Climbing Stairs

- **Link:** https://leetcode.com/problems/climbing-stairs/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** You can model this as a hierarchy of solver strategies — each subclass overrides a `solve(n)` method (recursive, memoized, iterative) — demonstrating polymorphism where the caller doesn't care which strategy it uses.
- **Hint:** The number of ways to reach step n depends only on the two steps before it. Think about what the base cases are.
- **Your file:** `leetcode_1.py`

---

## Problem 2 — Merge Two Sorted Lists

- **Link:** https://leetcode.com/problems/merge-two-sorted-lists/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** The `ListNode` class is a textbook example of an object that holds data (`val`) and a reference to another object of the same type (`next`) — the same pattern used in inheritance chains where each class knows about its parent.
- **Hint:** Think about what to do at each step: compare the heads of both lists and choose the smaller one. Consider what "merging" means when one list runs out first.
- **Your file:** `leetcode_2.py`

