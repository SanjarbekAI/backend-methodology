# L40 SQL LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Delete Duplicate Emails

- **Link:** https://leetcode.com/problems/delete-duplicate-emails/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** This problem requires a `DELETE` with a subquery or self-join — directly practicing the safe deletion patterns from today's lesson. It also demonstrates why `UNIQUE` constraints are valuable: they would have prevented duplicates from being inserted in the first place.
- **Hint:** You want to keep the row with the smallest `id` for each email and delete all others. A self-join comparing `id` values will help you identify which rows to delete.
- **Your file:** `leetcode_1.sql`

---

## Problem 2 — Second Highest Salary

- **Link:** https://leetcode.com/problems/second-highest-salary/
- **Difficulty:** 🟠 Medium
- **Why this lesson:** This problem requires using a subquery to exclude the maximum value and then find the next one — and it must return `NULL` if there is no second salary. It tests your understanding of subqueries and `NULL` handling, both of which are critical in real database work.
- **Hint:** Think about how `LIMIT` and `OFFSET` work together. Also consider: what happens if all salaries are the same? Your query must handle that edge case and return `NULL`.
- **Your file:** `leetcode_2.sql`

