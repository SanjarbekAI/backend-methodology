# L37 SQL LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Duplicate Emails

- **Link:** https://leetcode.com/problems/duplicate-emails/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** Finding duplicates requires grouping rows and filtering groups — a direct application of `GROUP BY` + `HAVING COUNT(*) > 1`. This is a data quality pattern you will use in every real PostgreSQL project.
- **Hint:** You cannot use `WHERE` to filter on aggregate functions like `COUNT()`. You need a different clause that filters after grouping.
- **Your file:** `leetcode_1.sql`

---

## Problem 2 — Rising Temperature

- **Link:** https://leetcode.com/problems/rising-temperature/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** This problem requires comparing each row to the **previous day's row** — a self-join pattern. It directly reinforces today's lesson on filtering and date comparisons, and previews the JOIN concept from the next lesson.
- **Hint:** Join the table to itself where the date difference is exactly one day. PostgreSQL's `INTERVAL '1 day'` or `DATE_PART` will help you compare dates.
- **Your file:** `leetcode_2.sql`

