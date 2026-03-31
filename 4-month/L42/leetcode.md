# L42 SQL LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Department Top Three Salaries

- **Link:** https://leetcode.com/problems/department-top-three-salaries/
- **Difficulty:** 🔴 Hard
- **Why this lesson:** This is the classic window function problem — it requires `DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC)` to rank employees within each department, then filtering for rank <= 3. This pattern is used constantly in real dashboards and leaderboards.
- **Hint:** Window functions cannot be filtered with `WHERE` directly. Use a CTE to compute the dense rank, then filter in the outer query. Remember `PARTITION BY` resets the rank counter for each department.
- **Your file:** `leetcode_1.sql`

---

## Problem 2 — Consecutive Numbers

- **Link:** https://leetcode.com/problems/consecutive-numbers/
- **Difficulty:** 🟠 Medium
- **Why this lesson:** This problem requires comparing each row to the next row and the one after — exactly the `LAG()` and `LEAD()` window function pattern from today's lesson. It is also solvable with a self-join approach, giving you practice with two different techniques.
- **Hint:** Use `LAG(num) OVER (ORDER BY id)` to access the previous row's value and `LEAD(num) OVER (ORDER BY id)` for the next row. A number appears 3 consecutive times if all three match. Wrap in a CTE and filter.
- **Your file:** `leetcode_2.sql`

