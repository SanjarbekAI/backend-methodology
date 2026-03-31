# Month 4 — Buggy Tasks

These tasks contain **intentionally broken SQL and Python code**. Your job is to find every bug, fix it, and make the program/query run correctly.

---

## When to do these

| Tasks | Give after |
|---|---|
| `bug_01.sql` `bug_02.sql` `bug_03.py` | After **L05** — you have covered Git basics, branching, PostgreSQL intro, SELECT/filtering/sorting, and JOINs |
| `bug_04.sql` `bug_05.py` `bug_06.py` | After **L09** — you have covered aggregations, GROUP BY, subqueries, DDL/constraints/indexes, psycopg2, and transactions |

---

## Rules

- Do **not** rewrite the query or program from scratch — fix only what is broken
- Every bug has a comment `-- BUG` (SQL) or `# BUG` (Python) next to it — but the comment does NOT tell you what the bug is
- Some tasks have **multiple bugs** — find all of them
- Write the number of bugs you found as a comment at the top of your fixed file
- Test your fix: the query must run without errors and return the expected result

---

## How to submit

Copy the buggy file, rename it `bug_01_fixed.sql` or `bug_01_fixed.py`, fix the bugs inside it, and submit the fixed version.

