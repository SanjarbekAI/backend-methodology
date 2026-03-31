# L16 Homework — Comprehensions & Functional Style

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. List comprehensions can always be rewritten as a `for` loop, but the reverse is not always true elegantly. Explain what makes a list comprehension more Pythonic than an equivalent loop. At what point does a comprehension become too complex and should be rewritten as a loop? Give an example of both a good comprehension and one that is too complex.

2. Compare list comprehensions, dict comprehensions, set comprehensions, and generator expressions. Describe a specific real-world use case for each type — not just a textbook example, but a situation you could encounter when building a real application.

3. There are two ways to use `if` inside a comprehension: as a filter at the end (`[x for x in lst if x > 0]`) and as a ternary inside the expression (`[x if x > 0 else 0 for x in lst]`). Explain the difference precisely — what each one does to the resulting list, and when you would use each one.

4. Generator expressions use `()` and are lazy — they compute values only when requested. Explain why this laziness is valuable and describe a real scenario where using a generator expression instead of a list comprehension could prevent a memory problem or improve performance significantly.

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

