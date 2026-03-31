# L43 SQL LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Game Play Analysis IV

- **Link:** https://leetcode.com/problems/game-play-analysis-iv/
- **Difficulty:** 🟠 Medium
- **Why this lesson:** This problem requires finding each player's first login date and checking if they logged in the next day — a pattern combining `MIN()`, date arithmetic, and self-joins or window functions. It directly mirrors the "first borrowing" and "overdue" date logic you built in today's library system.
- **Hint:** First find each player's first login date using `MIN(event_date)`. Then check if a record exists for `first_date + INTERVAL '1 day'`. Think about whether a JOIN or a subquery is cleaner here.
- **Your file:** `leetcode_1.sql`

---

## Problem 2 — Managers with at Least 5 Direct Reports

- **Link:** https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
- **Difficulty:** 🟠 Medium
- **Why this lesson:** This problem uses `GROUP BY` + `HAVING COUNT(*) >= 5` combined with a self-join — a direct application of the aggregation and self-join patterns from L39 and L38. In the library system, an analogous query would be "find members who have borrowed at least 5 books."
- **Hint:** You need to count how many employees report to each manager. Group by the manager's ID, filter for count >= 5, then join back to get the manager's name.
- **Your file:** `leetcode_2.sql`

