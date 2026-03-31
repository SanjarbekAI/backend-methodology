# L43 Tasks — Practice: Git Team Project

Complete the tasks below. Each task is a deliverable for the team project. Both developers contribute to each task through the Git workflow.

---

## Task 1 — Repository setup & first PR

**Scenario**
The project begins. Developer A creates the repository and the database schema. Developer B reviews it. This is the first time either of them has worked with someone else in the same Git repository — they need to establish the workflow from the start.

**Your task (Developer A)**
- Create a public GitHub repository named `library-management-system`
- Add a `.gitignore` for Python (include `venv/`, `__pycache__/`, `*.pyc`, `.env`)
- Add Developer B as a collaborator in GitHub Settings
- Create branch `feature/project-setup`
- Add: `requirements.txt` (`psycopg2-binary`, `python-dotenv`), `.env.example` (DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD with placeholder values)
- Commit with message `Add: project setup with requirements and env template`
- Push and open a Pull Request with a description explaining what was added
- After B reviews and approves, merge the PR

**Your task (Developer B)**
- Clone the repository after it's shared
- Review Developer A's PR — leave at least one comment (even if just "LGTM — approved")
- After merge: `git pull` on main
- Create branch `feature/database-schema`
- Write `migrations/001_create_tables.sql` with all 3 tables (books, members, borrowings) including all constraints and indexes
- Open PR — A reviews and merges

**Expected deliverable**
```
$ git log --oneline
c3d2e1f Docs: add README with setup steps
b2c1d0e Add: database schema migration 001
a1b0c9d Add: project setup with requirements and env template
```

**File:** Both developers submit a screenshot of the merged PRs and `git log --oneline`

---

## Task 2 — Parallel feature development (no conflicts)

**Scenario**
Both developers now work simultaneously on different parts of the codebase. They are on different branches touching different files — there should be no conflict. This is the ideal parallel workflow.

**Your task (Developer A)**
- Branch: `feature/book-repository`
- Create `db/connection.py` with a `get_connection()` function using `python-dotenv`
- Create `db/repositories/book_repo.py` with `BookRepository` class:
  - `get_all() → list[dict]`
  - `search(query: str) → list[dict]` — ILIKE on title and author
  - `create(title, author, isbn, genre, year, copies) → int`
  - `update_available(book_id, delta: int) → bool` — add or subtract available copies
  - `delete(book_id) → bool`
- Write a quick test at the bottom under `if __name__ == "__main__":` that inserts 3 books and prints them
- Commit twice (after BookRepo skeleton, after adding test) → PR → merge

**Your task (Developer B)**
- Branch: `feature/member-repository`
- Create `db/repositories/member_repo.py` with `MemberRepository`:
  - `get_all(active_only=True) → list[dict]`
  - `get_by_email(email: str) → dict | None`
  - `create(full_name, email, phone) → int`
  - `deactivate(member_id) → bool`
- Write test at the bottom: insert 2 members, get by email, deactivate one
- Two commits → PR → merge

**Expected deliverable**
Both PRs merged cleanly with no conflicts. Final file structure:
```
library-management-system/
  db/
    connection.py
    repositories/
      book_repo.py
      member_repo.py
  migrations/
    001_create_tables.sql
```

**File:** `db/repositories/book_repo.py` and `db/repositories/member_repo.py`

---

## Task 3 — Intentional conflict resolution

**Scenario**
Both developers need to edit `main.py` to wire up their features. They both create their branches from `main` at the same time, both edit the same section of `main.py`, and when Developer B tries to merge, there is a conflict. This is the most important Git skill to practice.

**Your task**
- Developer A: branch `feature/main-menu-books`, write `main.py` with a menu loop. Add menu options 1–4 for book operations (view, search, add, delete). Commit and merge first.
- Developer B: branch `feature/main-menu-members`, starting from the SAME `main` commit as A (before A's merge). Add menu options 5–7 for member operations in `main.py` at the same location.
- B tries to merge → **conflict occurs** in `main.py`
- Together, resolve the conflict so the final `main.py` has ALL menu options (1–4 for books, 5–7 for members) in one clean menu
- Commit the resolution with message `Merge: combine book and member menu options`
- Run `git log --oneline --graph` and show the diverge + merge point

**Expected deliverable**
```
$ git log --oneline --graph
*   f3e2d1c Merge: combine book and member menu options
|\
| * d2c1b0a Add: member management menu options (5-7)
* | c1b0a9f Add: book management menu options (1-4)
|/
* b0a9f8e Add: member-repository with full CRUD
```

**File:** Final `main.py` with all menu options

---

## Task 4 — Borrowing system with transactions

**Scenario**
Developer B builds the most critical part of the system: the borrowing workflow. Borrowing a book requires two database writes that must be atomic — if either fails, both must roll back. This is real multi-step transaction logic, not a tutorial exercise.

**Your task (Developer B)**
- Branch: `feature/borrowing-system`
- Create `db/repositories/borrowing_repo.py` with `BorrowingRepository`:
  - `borrow(book_id, member_id, days=14) -> int`
    - Verify book exists and `available_copies > 0` — raise `ValueError` if not
    - `BEGIN` → `UPDATE books SET available_copies = available_copies - 1` → `INSERT INTO borrowings` → `COMMIT`
    - Returns the new borrowing id
  - `return_book(borrowing_id) -> bool`
    - `BEGIN` → `UPDATE borrowings SET returned_at = NOW()` → `UPDATE books SET available_copies = available_copies + 1` → `COMMIT`
  - `get_active() -> list[dict]` — JOIN with books and members
  - `get_overdue() -> list[dict]` — `due_date < CURRENT_DATE AND returned_at IS NULL`
- All multi-step operations wrapped in try/except with `conn.rollback()` on failure
- PR → Developer A reviews → merge

**Expected output** (when wired into main menu)
```
=== Active Borrowings ===
  #3 | "Clean Code" (2 copies left) | Sardor Toshev | Due: 2025-02-10
  #5 | "Python Tricks" (0 copies left) | Nilufar Karimova | Due: 2025-02-05

=== Overdue ===
  #1 | "The Pragmatic Programmer" | Aziz Karimov | Was due: 2025-01-20 (11 days ago)
```

**File:** `db/repositories/borrowing_repo.py`

---

## Task 5 — Final integration & daily report

**Scenario**
The system is almost complete. The final task is to wire everything together in `main.py`, add the daily summary report, write the README, and do a final end-to-end test as a team. The product is "shipped" when you can run `python main.py` and use every feature without errors.

**Your task (both developers)**
- Developer A: Branch `feature/daily-report`
  - Add menu option to show the daily summary:
    ```sql
    SELECT
        (SELECT COUNT(*) FROM books) AS total_books,
        (SELECT COUNT(*) FROM members WHERE is_active) AS active_members,
        (SELECT COUNT(*) FROM borrowings WHERE returned_at IS NULL) AS active_borrowings,
        (SELECT COUNT(*) FROM borrowings WHERE due_date < CURRENT_DATE AND returned_at IS NULL) AS overdue
    ```
  - Print the result as a formatted dashboard
- Developer B: Branch `feature/readme`
  - Write a complete `README.md`:
    - Project description
    - Setup instructions (clone → create venv → install → configure .env → run migrations → run app)
    - `.env.example` contents
    - Screenshot of the terminal menu
- Both merge their branches
- Both run `python main.py` on their own machine and demonstrate ALL features working
- Final command: `git log --oneline --graph --all` — count the total commits as a team

**Expected final menu**
```
=== Library Management System ===
1. View all books
2. Search books
3. Add a book
4. Delete a book
5. View all members
6. Add a member
7. Deactivate a member
8. Borrow a book
9. Return a book
10. Active borrowings
11. Overdue books
12. Daily summary
0. Exit
```

**File:** Final `main.py` + `README.md` — submitted as a GitHub repository link

