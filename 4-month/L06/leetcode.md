# L39 SQL LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Not Boring Movies

- **Link:** https://leetcode.com/problems/not-boring-movies/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** This problem combines filtering with `WHERE` and sorting — reinforcing today's lesson on how row-level filters interact with ordering. It also requires understanding odd/even logic in SQL, which is common in data cleaning scenarios.
- **Hint:** You need two conditions in your `WHERE` clause — one for the ID and one for the description. Think about how to check if a number is odd using the modulo operator `%`.
- **Your file:** `leetcode_1.sql`

---

## Problem 2 — Average Selling Price

- **Link:** https://leetcode.com/problems/average-selling-price/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** This problem requires a `JOIN` combined with `GROUP BY` and `AVG()` — exactly the aggregation-over-joined-tables pattern you practiced in today's tasks. It also introduces weighted averages, which appear constantly in real pricing and analytics systems.
- **Hint:** The average price is not a simple `AVG(price)` — it must be weighted by the number of units sold. Think about `SUM(price * units) / SUM(units)`.
- **Your file:** `leetcode_2.sql`

