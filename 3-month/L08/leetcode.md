# L30 LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Implement Trie (Prefix Tree)

- **Link:** https://leetcode.com/problems/implement-trie-prefix-tree/
- **Difficulty:** 🟡 Medium
- **Why this lesson:** Each `TrieNode` controls its own children dict creation — similar to how `__new__` in a metaclass controls class creation. Understanding how objects create and manage their sub-objects is the same mental model.
- **Hint:** A Trie node needs two things: a dictionary of its children and a flag marking whether it ends a word. Insert and search both walk the trie character by character.
- **Your file:** `leetcode_1.py`

---

## Problem 2 — Design Log Storage System

- **Link:** https://leetcode.com/problems/design-log-storage-system/
- **Difficulty:** 🟡 Medium
- **Why this lesson:** The retrieval method mirrors how a context manager scopes operations — you define a range (granularity) and only events within that scope are returned, just like `__enter__` and `__exit__` define the boundaries of managed execution.
- **Hint:** Store logs as `(timestamp_string, log_id)` tuples. For retrieval, you can truncate the timestamp string to the required granularity and do string comparison — no date parsing needed.
- **Your file:** `leetcode_2.py`

