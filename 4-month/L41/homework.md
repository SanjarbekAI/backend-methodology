# L41 Homework — PostgreSQL + Python (psycopg2)

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. Explain what **SQL injection** is, how it works, and why it is considered one of the most critical security vulnerabilities in web applications. Show (in words, not code) what an attacker could do with a vulnerable query. Then explain exactly how **parameterized queries** prevent this attack.

2. psycopg2 returns rows as tuples by default, but `RealDictCursor` returns them as dictionaries. Compare these two approaches — when is each one more appropriate? Describe a real scenario where using tuples would cause a maintenance problem as the codebase grows.

3. Explain the concept of **commit** and **rollback** in database transactions. Why does psycopg2 not auto-commit by default? Describe a real multi-step operation (like a bank transfer or an order placement) where forgetting to rollback on failure could leave the database in an inconsistent state.

4. The **Repository pattern** separates database access logic from business logic. Explain the benefit of this separation using a concrete example: if you later switch from psycopg2 to SQLAlchemy, how does the Repository pattern limit how much code you need to change? What would happen in a codebase without this pattern?

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

