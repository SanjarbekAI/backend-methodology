# L32 Homework — Practice: Advanced Topics

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. In today's project, you combined `asyncio`, context managers, metaclasses, generators, `lru_cache`, and `__slots__` in a single system. Looking back, which two of these advanced features interacted in the most interesting or unexpected way? Describe the interaction and explain what you learned from it.

2. The `RateLimiter` context manager controls access to a shared resource (the network). Compare this to the `Lock` you used in threading. Both control concurrent access — what is fundamentally different about the problem each one solves, and what would happen if you accidentally applied the wrong tool to each problem?

3. The project used a metaclass for plugin registration and `@lru_cache` for caching — both are "invisible" features that work at the framework level rather than the application level. Describe the difference between "framework-level" code and "application-level" code. Why do framework features like metaclasses and caching need to be invisible to the caller?

4. After profiling, you identified the bottlenecks and optimized them. Describe your profiling process: what did you measure, what did you find, and what change produced the biggest improvement? If you had 2 more hours on this project, what would you optimize next and why?

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

