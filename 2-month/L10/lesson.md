# L21 — Practice: Functions

## Project brief
You are building a **command-line task management tool** — a simplified to-do app for developers. The entire application must be built using functions: closures for configuration, decorators for logging, generators for ID creation, and comprehensions for data processing. No classes yet — pure functional design.

---

## Requirements

1. A menu-driven CLI loop with options: Add Task, View Tasks, Complete Task, Delete Task, Filter by Priority, Save, Exit
2. Each task has: `id` (auto-generated), `title`, `priority` (`low`/`medium`/`high`), `status` (`open`/`done`), `created_at`
3. Use a **generator** to create sequential task IDs (`TASK-0001`, `TASK-0002`, ...)
4. Use a **decorator** to log every function call that modifies the task list
5. Use a **closure** to create a priority-filter function (e.g., `filter_high = make_priority_filter("high")`)
6. Use **comprehensions** for all list filtering and transformation operations
7. All functions must have **type hints**
8. Save and load tasks as **JSON**

---

## Milestones

**Milestone 1 (0:00–0:30) — Core data layer**
- Build the ID generator
- Build `add_task`, `complete_task`, `delete_task` functions with the logging decorator
- Test all three in isolation with print statements

**Milestone 2 (0:30–1:00) — Query & display layer**
- Build `get_all_tasks`, `get_open_tasks`, `get_done_tasks` using comprehensions
- Build `make_priority_filter` closure and the 3 filter functions
- Build `display_tasks` — prints a formatted table

**Milestone 3 (1:00–1:30) — Persistence layer**
- Build `save_tasks(filepath)` and `load_tasks(filepath)` using JSON
- Handle `FileNotFoundError` on first run

**Milestone 4 (1:30–2:00) — CLI integration & polish**
- Wire everything together in the `main()` function with the menu loop
- Add the `if __name__ == "__main__":` guard
- Test end-to-end: add tasks, filter, complete, save, reload

---

## Bonus challenges

1. **Sort options:** Add the ability to view tasks sorted by priority (high first) or by creation date.
2. **Search:** Add a menu option to search tasks by keyword in the title using a generator expression.
3. **Stats:** Add a function that prints stats: total tasks, open vs done, tasks per priority — using dict comprehensions.

