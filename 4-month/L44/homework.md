# L44 Homework — Practice: Full Terminal App with PostgreSQL

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. Reflect on the StoreOS `place_order` transaction. You needed to perform 4 separate database writes atomically. Describe the exact sequence of operations, explain why each one could fail independently, and explain what state the database would be in after each possible failure point if you had NOT used a transaction.

2. The `unit_price` column in `order_items` stores a snapshot of the product's price at the time of ordering — not a foreign key to the current price. Explain why this design decision is correct from a business perspective. What reports or calculations would be permanently broken if you stored only the `product_id` and always read the current price?

3. You used the Repository pattern to separate database logic from application logic. Looking back at your own code: if the business decided to switch from psycopg2 to SQLAlchemy next month, which files would need to change and which would stay exactly the same? What does this tell you about the value of the pattern?

4. Compare your StoreOS terminal app to the JSON file-based programs you built in Month 2. Identify at least 3 specific scenarios where the PostgreSQL-backed version is meaningfully better — not just "faster" in the abstract, but in ways that would matter to a real business user like Dilnora.

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

