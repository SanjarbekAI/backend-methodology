# L37 Homework — SQL: SELECT, Filtering & Sorting

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. Explain why `SELECT *` is considered bad practice in production application code, even though it is convenient during development. Describe a real scenario where using `SELECT *` could cause a bug or performance problem in a live application.

2. In SQL, `NULL` represents the absence of a value — not zero, not an empty string, not `False`. Explain why `WHERE phone = NULL` never returns any rows, and what you must write instead. Give a real example of a column in a business database where `NULL` has a specific meaningful interpretation (not just "missing data").

3. Compare `WHERE ... LIKE` and `WHERE ... ILIKE` in PostgreSQL. When would you use each one? Describe a real search feature in an app — like a name search field — where choosing `LIKE` instead of `ILIKE` could lead to a frustrating user experience.

4. Explain the purpose of `LIMIT` and `OFFSET` in SQL. How do they work together to implement **pagination** in an API? If a table has 10,000 rows and your API returns 20 per page, write out the SQL for pages 1, 2, and 50 in your explanation.

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

