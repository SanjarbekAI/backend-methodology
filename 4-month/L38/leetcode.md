# L38 SQL LeetCode Problems

Try to solve these after finishing the lesson tasks. Focus on understanding the problem first — read it twice before writing any code.

---

## Problem 1 — Combine Two Tables

- **Link:** https://leetcode.com/problems/combine-two-tables/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** This is the classic LEFT JOIN problem — you must return all persons even if they have no address record. It directly mirrors the "customers with no orders" pattern from today's tasks.
- **Hint:** Think about which table must be on the left side — the one where you need all rows, even unmatched ones.
- **Your file:** `leetcode_1.sql`

---

## Problem 2 — Customer Who Visited but Did Not Make Any Transactions

- **Link:** https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
- **Difficulty:** 🟢 Easy
- **Why this lesson:** This is the LEFT JOIN + `WHERE right_table.id IS NULL` pattern — the "ghost customer" technique you practiced in Task 2. It's one of the most useful JOIN patterns in backend development.
- **Hint:** JOIN the visits table to the transactions table. Visits that have no matching transaction will have NULL on the transaction side — filter for exactly those.
- **Your file:** `leetcode_2.sql`

