# L41 SQL LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Nth Highest Salary

- **Link:** https://leetcode.com/problems/nth-highest-salary/
- **Difficulty:** 🟠 Medium
- **Why this lesson:** This problem requires writing a SQL function — a concept directly related to building reusable database logic, which mirrors the Repository pattern you practiced today. It also uses `LIMIT` + `OFFSET` in a non-trivial way.
- **Hint:** To get the Nth highest, you can use `ORDER BY ... DESC LIMIT 1 OFFSET N-1` after eliminating duplicates with `DISTINCT`. Handle the edge case where N is larger than the number of distinct salaries.
- **Your file:** `leetcode_1.sql`

---

## Problem 2 — Rank Scores

- **Link:** https://leetcode.com/problems/rank-scores/
- **Difficulty:** 🟠 Medium
- **Why this lesson:** This problem introduces **window functions** — one of the most powerful SQL features you'll use when building analytics and reporting queries from Python. The `DENSE_RANK()` window function is exactly what's needed here.
- **Hint:** Window functions use the `OVER (ORDER BY ...)` syntax. `DENSE_RANK()` gives the same rank to ties and doesn't skip numbers — unlike `RANK()`. Try both and observe the difference.
- **Your file:** `leetcode_2.sql`

