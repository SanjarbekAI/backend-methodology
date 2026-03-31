# L36 SQL LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Invalid Tweets

- **Link:** https://leetcode.com/problems/invalid-tweets/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** This problem uses `LENGTH()` — a built-in SQL function — to filter rows based on the size of a text column. This is exactly the kind of data validation you would add to a real PostgreSQL table via a `CHECK` constraint or query.
- **Hint:** You need to find rows where the content is longer than a specific number of characters. SQL has a built-in function that counts string length.
- **Your file:** `leetcode_1.sql`

---

## Problem 2 — Employees Earning More Than Their Managers

- **Link:** https://leetcode.com/problems/employees-earning-more-than-their-managers/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** This problem requires you to compare a row to another row in the **same table** — the employee's salary versus their manager's salary. This is a preview of self-joins, which you'll use heavily when your tables have foreign keys pointing back to themselves.
- **Hint:** You need to join the `Employee` table to itself — once as the employee and once as the manager — then compare their salaries.
- **Your file:** `leetcode_2.sql`

