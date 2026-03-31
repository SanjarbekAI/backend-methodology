# L31 Homework — Performance & Memory

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. The golden rule of optimization is "profile first, optimize second." Explain why optimizing without profiling is dangerous. Describe a real scenario where a developer spent hours optimizing the wrong part of the code. What does `cProfile` tell you that visual code inspection cannot?

2. `__slots__` reduces memory usage per instance by replacing the instance `__dict__` with a fixed-size structure. Explain why the default `__dict__` approach exists at all — what flexibility does it provide? Describe a situation where `__slots__` would be the right choice and a situation where it would be the wrong choice.

3. `functools.lru_cache` is described as "memoization." Explain what memoization is, what type of functions benefit from it, and what type of functions it must NOT be used on. Why does using `lru_cache` on methods with `self` create a memory leak?

4. Big O notation describes how performance scales with input size. Explain why O(n²) is acceptable for 100 items but catastrophic for 1,000,000 items. Describe a real backend scenario — such as a search system, a recommendation engine, or a reporting tool — where the wrong algorithmic complexity would make the feature unusable at production scale.

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

