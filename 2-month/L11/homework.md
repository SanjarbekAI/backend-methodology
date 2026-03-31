# L22 Homework — Practice: Intermediate Review

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. This project split the code into `models.py`, `storage.py`, and `main.py`. Reflect on this structure: what are the benefits of this separation? Describe what would happen to the project's maintainability if all the code were in one file. How does this relate to professional software architecture?

2. Dataclasses with `__post_init__` validation and RegEx validators both serve to ensure data quality. Compare these two approaches — when is each one the right tool? Could you validate an email format inside `__post_init__`? What are the trade-offs of doing all validation inside the dataclass versus in a separate validator function?

3. Converting between dataclasses and JSON requires serialization and deserialization. Describe the challenge this creates: dataclasses are Python objects, JSON understands only basic types. How did you solve this? What would break if you tried to call `json.dumps()` directly on a dataclass instance?

4. Looking back at all of Month 2 — functions, closures, decorators, generators, comprehensions, modules, RegEx, JSON, type hints, and dataclasses — identify the two concepts that changed how you think about writing code the most. Explain specifically how each one changed your approach, with a concrete example from a task or project.

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

