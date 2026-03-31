# L26 LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Design HashMap

- **Link:** https://leetcode.com/problems/design-hashmap/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** Start by defining the abstract interface (put, get, remove) before any implementation — this is the interface-first design that abstract classes and protocols enforce.
- **Hint:** You don't need to use Python's built-in dict. Think about what data structure you would use to store key-value pairs manually, and how to handle collisions.
- **Your file:** `leetcode_1.py`

---

## Problem 2 — LRU Cache

- **Link:** https://leetcode.com/problems/lru-cache/
- **Difficulty:** 🟡 Medium
- **Why this lesson:** Define the contract first (`get` and `put` with O(1) complexity), then choose the internal data structures — this is exactly the workflow of abstract class design where the interface is fixed but the implementation is free.
- **Hint:** You need both fast lookup AND ordered access. Think about combining two data structures — one for speed, one for order.
- **Your file:** `leetcode_2.py`

