# L31 LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Top K Frequent Elements

- **Link:** https://leetcode.com/problems/top-k-frequent-elements/
- **Difficulty:** 🟡 Medium
- **Why this lesson:** The naive O(n log n) approach sorts the whole frequency map. The optimal O(n) bucket sort approach demonstrates exactly the kind of algorithmic improvement that profiling leads you to — same result, dramatically different scaling behavior.
- **Hint:** Instead of sorting by frequency, think about using frequency as an index into a bucket array. The maximum possible frequency is n (if all elements are the same).
- **Your file:** `leetcode_1.py`

---

## Problem 2 — Find Median from Data Stream

- **Link:** https://leetcode.com/problems/find-median-from-data-stream/
- **Difficulty:** 🔴 Hard
- **Why this lesson:** Every design decision here is a performance decision — O(n) insert vs O(log n) insert, O(n) median vs O(1) median. Applying `cProfile` thinking: what operation is called most frequently and must be fastest?
- **Hint:** Use two heaps: a max-heap for the lower half and a min-heap for the upper half. Keep them balanced in size. The median is either the top of one heap or the average of both tops.
- **Your file:** `leetcode_2.py`

