# L25 Homework — OOP: Encapsulation & Magic Methods

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. Encapsulation is described as "hiding implementation details and exposing only what is necessary." Explain why this is valuable in a large codebase. Give a concrete example of what could go wrong in a real system — such as a banking app, an inventory system, or a user authentication service — if internal state could be modified freely from outside the class.

2. Python uses naming conventions (`_x` and `__x`) rather than enforced access modifiers like `private` in Java. Explain the difference between single and double underscore prefixes, and discuss the philosophy behind Python's approach. Is the lack of true enforcement a weakness or a feature? Support your answer with reasoning.

3. The `@property` decorator allows you to expose an attribute while controlling how it is read and written. Explain how `@property` combined with `@setter` provides better encapsulation than exposing the raw attribute directly. Give an example of a validation rule that would be impossible to enforce without a setter.

4. Magic methods (dunder methods) allow custom classes to integrate with Python's built-in syntax. Explain why this is powerful — what does it mean for a custom class to "feel native" to Python? Compare having `__len__` vs a regular `get_count()` method. Why would a developer choose one approach over the other?

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

