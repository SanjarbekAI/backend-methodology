# L44 SQL LeetCode Problems

Try to solve these after finishing the lesson tasks. These are harder problems — take your time, read carefully, and think before coding.

---

## Problem 1 — Human Traffic of Stadium

- **Link:** https://leetcode.com/problems/human-traffic-of-stadium/
- **Difficulty:** 🔴 Hard
- **Why this lesson:** This problem requires finding 3 or more consecutive rows meeting a condition — a direct application of window functions (`ROW_NUMBER()` with grouping tricks) or self-joins. It is the kind of sequential analysis query you would write in a real StoreOS report: "find 3 or more consecutive days with orders over a threshold."
- **Hint:** One clean approach: subtract `ROW_NUMBER() OVER (ORDER BY id)` from `id` — for consecutive rows meeting the condition, this difference is constant. Group by this difference and filter groups with 3+ rows.
- **Your file:** `leetcode_1.sql`

---

## Problem 2 — Exchange Seats

- **Link:** https://leetcode.com/problems/exchange-seats/
- **Difficulty:** 🟠 Medium
- **Why this lesson:** This problem uses `CASE WHEN` with row number logic and modulo arithmetic to transform data — exactly the pattern used in your StoreOS reports for formatting and classification. It tests whether you can use SQL as a transformation tool, not just a retrieval tool.
- **Hint:** Use `CASE WHEN id % 2 = 1 THEN id + 1 ELSE id - 1 END` to swap seat IDs, but handle the edge case when the last seat has an odd id (no one to swap with).
- **Your file:** `leetcode_2.sql`

