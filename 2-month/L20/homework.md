# L20 Homework — Type Hints & Dataclasses

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. Python does not enforce type hints at runtime — the program still runs even if you pass the wrong type. Given this, why do professional developers still add type hints to all their code? Describe at least three concrete benefits of type hints beyond just "documentation."

2. The `@dataclass` decorator automatically generates `__init__`, `__repr__`, and `__eq__`. Explain what each of these three methods does, why they are necessary for a data object, and describe the pain a developer would experience writing these manually for every class in a large project.

3. Using a mutable default value like `items: list = []` in a dataclass raises a `ValueError` in Python. Explain why this restriction exists — what actual bug would occur if Python allowed it? How does `field(default_factory=list)` solve the problem?

4. `Optional[str]` and `str | None` are two ways to express the same type hint. Describe a real function in a backend application where the return type should be `Optional` — where the function might return a value or return nothing. Why is it important to explicitly declare this in the type hint instead of leaving it unspecified?

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

