# L29 Homework — Concurrency: Threading & Async

**Student name:**
**Date:**
**Lesson date:**

---

## Questions

1. Explain the difference between concurrency and parallelism. Python's `threading` module does not achieve true CPU parallelism due to the GIL (Global Interpreter Lock). Explain what the GIL is, why it exists, and why threading is still useful and performant despite the GIL for the kinds of programs Python developers typically write.

2. A race condition is a bug that only appears sometimes — it depends on timing. Explain why this makes race conditions especially dangerous and difficult to debug. Describe a real-world scenario in a financial or e-commerce system where a race condition could cause a serious business problem, and explain how a `Lock` would prevent it.

3. `asyncio` and `threading` both enable concurrency but work in fundamentally different ways. Compare the two approaches: what is cooperative multitasking versus preemptive multitasking? Describe a type of application where `asyncio` would be the clearly superior choice over threads, and explain why.

4. The `async/await` syntax requires that `await` only be used inside `async def` functions, and async functions must be run with `asyncio.run()`. Explain why this creates an "async boundary" that propagates through a codebase. What happens when you need to call an async function from synchronous code deep in a call stack?

---

## Reflection

1. What was the hardest part of this lesson for you?

2. Write one real situation from your daily life where you could use what you learned today.

3. What question do you still have that was not answered in the lesson?

