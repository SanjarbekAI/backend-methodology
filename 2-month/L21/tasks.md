# L21 Tasks — Practice: Functions

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The task manager (main project)

**Scenario**
A development team needs a personal task tracker they can run from the terminal. It must be built purely with functions — closures, decorators, generators, comprehensions, type hints, and JSON persistence.

**Your task**
- Build the full task manager as described in `lesson.md`
- The app must have a working menu loop with all 6 options
- ID generation must use a generator
- Logging must use a decorator applied to add/complete/delete functions
- Priority filtering must use a closure-based filter factory
- All list processing must use comprehensions
- Data must persist between runs via JSON

**Expected flow**
```
=== Task Manager ===
Loaded 3 existing tasks.

1. Add Task        4. Delete Task
2. View Tasks      5. Filter by Priority
3. Complete Task   6. Save & Exit

> 2

ID         Title                  Priority  Status  Created
TASK-0001  Fix login bug          high      done    2026-03-28
TASK-0002  Write API docs         medium    open    2026-03-29
TASK-0003  Refactor auth module   high      open    2026-03-30
```

**File:** `task_01.py`

---

## Task 2 — The data processing pipeline

**Scenario**
A sales analyst needs to process a list of raw sales records using a purely functional pipeline: validate, transform, filter, aggregate — each step is a separate typed function.

**Your task**
- Define a list of 10 sales records: `{"rep": str, "product": str, "amount": float | str, "region": str}`
  (include some invalid entries: `amount = "N/A"` or negative)
- Write these typed functions:
  - `validate_records(records: list[dict]) -> list[dict]` — removes invalid
  - `normalize_amounts(records: list[dict]) -> list[dict]` — ensures all amounts are floats
  - `filter_by_region(records: list[dict], region: str) -> list[dict]` — closure-based
  - `total_by_rep(records: list[dict]) -> dict[str, float]` — aggregates using dict comprehension
- Chain them and print the final summary

**Expected output**
```
Valid records: 7/10
Region "North" records: 3

Revenue by rep:
  Ali:   4,250,000 sum
  Sara:  3,100,000 sum
  Bobur: 6,800,000 sum
```

**File:** `task_02.py`

