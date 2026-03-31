# L28 LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Design Parking System

- **Link:** https://leetcode.com/problems/design-parking-system/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** A clean SRP class with one job: track spaces per type. Model it as you would in the hotel system — focused, encapsulated, with a clear interface.
- **Hint:** You need three counters and one method. The car `type` directly maps to which counter to check and decrement.
- **Your file:** `leetcode_1.py`

---

## Problem 2 — Design Twitter

- **Link:** https://leetcode.com/problems/design-twitter/
- **Difficulty:** 🟡 Medium
- **Why this lesson:** Applies SRP (tweets, follows, and feed are separate concerns), OCP (the feed algorithm can be swapped), and DIP (the storage could be any backend). A complete OOP design exercise.
- **Hint:** For the news feed, you need the 10 most recent tweets from users you follow. Think about what data structure gives you efficient merging of multiple tweet lists.
- **Your file:** `leetcode_2.py`

