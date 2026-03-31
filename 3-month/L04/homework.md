# L26 Homework — Abstract Classes & Interfaces

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. Abstract classes cannot be instantiated directly — they exist only to be subclassed. Explain why this restriction is valuable in a real project. Describe a scenario where having a concrete base class (one that can be instantiated) instead of an abstract one could lead to subtle bugs or design problems.

2. Compare Python's `ABC` with `Protocol`. Describe the key differences in how they enforce contracts, what they require from implementing classes, and when each one is the right tool. Give a real example of a situation where you would specifically choose `Protocol` over `ABC`.

3. Abstract classes define a "contract" between the designer of a system and the developers who extend it. Explain what this contract means in practice: what obligations does it create? How does an abstract class improve a team's ability to work in parallel on different implementations of the same interface?

4. The `@abstractmethod` decorator raises a `TypeError` only when you try to instantiate a subclass that hasn't implemented all abstract methods — not when you define the incomplete subclass. Explain why this design choice is somewhat dangerous. What would be a better developer experience, and how do tools like `mypy` help fill this gap?

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

