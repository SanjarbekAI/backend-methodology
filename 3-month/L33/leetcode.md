# L33 LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Design In-Memory File System

- **Link:** https://leetcode.com/problems/design-in-memory-file-system/
- **Difficulty:** 🔴 Hard
- **Why this lesson:** A capstone OOP design problem — requires a clean class hierarchy, encapsulation, and the same kind of multi-concept integration you applied in PyStore: nested structures, path traversal, and content storage all in one system.
- **Hint:** Each directory node needs to store both its subdirectory nodes and its file contents. A `TrieNode`-style structure works well — each node is a dict of children plus an optional file content string.
- **Your file:** `leetcode_1.py`

---

## Problem 2 — Word Search II

- **Link:** https://leetcode.com/problems/word-search-ii/
- **Difficulty:** 🔴 Hard
- **Why this lesson:** Combines the Trie data structure (from L30), backtracking algorithm design, and performance optimization — every word-pruning decision is a Big O decision. This is the kind of problem that rewards all three months of thinking.
- **Hint:** Build a Trie from the word list first. Then DFS the board, pruning any path that doesn't have a Trie node. Mark visited cells during recursion and restore them on backtrack.
- **Your file:** `leetcode_2.py`

