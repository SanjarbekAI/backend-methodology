# L15 Homework — Decorators & Generators

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. A decorator modifies a function's behaviour without changing its source code. Explain why this principle — adding behaviour without modifying the original — is valuable in software development. Give two real examples from web frameworks or professional applications where this pattern is used (hint: think about authentication, logging, caching, or rate limiting).

2. Explain what `@functools.wraps(func)` does inside a decorator wrapper and why it matters. What specific problems occur if you forget to include it? Give a concrete example of debugging that would be made harder without it.

3. Generators use `yield` instead of `return` and compute values one at a time. Explain why this is more memory-efficient than returning a full list. Describe a real-world scenario where using a generator instead of a list would make a significant difference in terms of memory usage or performance.

4. Compare a generator expression `(x**2 for x in range(n))` with a list comprehension `[x**2 for x in range(n)]`. When is each one the correct choice? Describe a situation where choosing the wrong one could cause a program to run out of memory or fail entirely.

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

