# L30 Homework — Context Managers & Metaclasses

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. Context managers guarantee resource cleanup using the `with` statement. Explain what "guaranteed cleanup" means technically — what exactly does Python do when the `with` block exits, whether normally or with an exception? Compare this to the manual `open()`/`close()` pattern and describe a real scenario where forgetting to close a resource could cause a production problem.

2. `__exit__` receives three arguments: `exc_type`, `exc_val`, and `exc_tb`. Explain what each one contains, when they are `None` versus populated, and what the return value of `__exit__` controls. Give a real example of a context manager where you would deliberately return `True` from `__exit__` and explain why that decision was made.

3. In Python, `type` is the metaclass of all classes. Explain what this means — what is the relationship between a class, its metaclass, and an instance? Use a concrete analogy or diagram-in-words to explain the three-level hierarchy: metaclass → class → instance.

4. Metaclasses are described as "solving problems at the class creation level." Explain what this means in practice — give two real examples from popular Python frameworks (such as Django, SQLAlchemy, or Pydantic) where metaclasses are used behind the scenes. Why would you use a metaclass over a class decorator for these use cases?

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

