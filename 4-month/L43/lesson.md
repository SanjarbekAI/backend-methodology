# L43 — Practice: Git Team Project

## Project brief
You are part of a **2-person development team** building a command-line **Library Management System**. The system tracks books, members, and borrowings in a PostgreSQL database. Today's session is 100% about working like a real team: branching, reviewing, merging, resolving conflicts, and maintaining a clean commit history — all while building a working Python + PostgreSQL application together.

Each student takes one role at the start, then switches halfway. Both roles contribute code via feature branches and Pull Requests.

---

## Roles

**Developer A — Core database layer**
Responsible for: database schema SQL, `db/connection.py`, `db/repositories/book_repo.py`, `db/repositories/member_repo.py`

**Developer B — Application layer**
Responsible for: `db/repositories/borrowing_repo.py`, `app/menu.py`, `app/handlers.py`, `main.py`

Both developers share: `.env.example`, `requirements.txt`, `README.md`, `migrations/`

---

## System requirements

The finished system must:
1. Connect to PostgreSQL using `psycopg2` with credentials from a `.env` file
2. Store books (id, title, author, isbn, genre, total_copies, available_copies)
3. Store members (id, full_name, email, phone, joined_at, is_active)
4. Store borrowings (id, book_id, member_id, borrowed_at, due_date, returned_at)
5. Support full CRUD for books and members via the terminal menu
6. Allow borrowing a book: reduces `available_copies`, creates borrowing record
7. Allow returning a book: increases `available_copies`, sets `returned_at`
8. Show currently borrowed books (unreturned) with member and due date
9. Show overdue books: `due_date < TODAY` and `returned_at IS NULL`
10. Generate a daily summary: total books, total members, active borrowings, overdue count

---

## Git workflow rules (mandatory)

- `main` branch is protected — never commit directly to it
- Every feature lives on a branch named: `feature/<short-description>`
- Every branch must have a Pull Request before merging
- Minimum 2 commits per feature branch
- Commit messages must follow: `Add:`, `Fix:`, `Refactor:`, `Test:`, `Docs:`
- After merging, delete the feature branch

---

## Milestones

**Milestone 1 (0:00–0:25) — Setup & schema**
- Developer A: Create the GitHub repository, add Developer B as collaborator
- Both: Clone the repo, create `venv`, install `psycopg2-binary python-dotenv`, commit `requirements.txt`
- Developer A: Create branch `feature/database-schema`, write `migrations/001_create_tables.sql`, push and open PR
- Developer B: Review and approve the PR, merge it
- Both: `git pull` on main

**Milestone 2 (0:25–0:55) — Repository layer**
- Developer A: Branch `feature/book-repo` → write `BookRepository` class with get_all, get_by_id, search, create, update_copies, delete → PR → merge
- Developer B: Branch `feature/member-repo` → write `MemberRepository` with get_all, get_by_email, create, deactivate → PR → merge
- Both: `git pull` and test their own repositories work against the live database

**Milestone 3 (0:55–1:25) — Application layer**
- Developer B: Branch `feature/borrow-system` → write `BorrowingRepository` with borrow(), return_book(), get_active(), get_overdue() → PR → merge
- Developer A: Branch `feature/terminal-menu` → write `main.py` with a full menu loop calling all repository methods → PR → merge
- Intentionally create a conflict on `menu.py` by both editing it simultaneously → resolve the conflict together → merge

**Milestone 4 (1:25–2:00) — Polish & documentation**
- Developer A: Branch `feature/daily-report` → add a daily summary command to the menu
- Developer B: Branch `feature/readme` → write a complete `README.md` with setup instructions, `.env.example`, and usage examples
- Both: Run the final application end-to-end — borrow a book, return it, check overdue list, view daily summary
- Final `git log --oneline --graph --all` — review the full team history together

---

## Bonus challenges
1. Add a `CHECK` constraint that prevents `available_copies` from going negative — and handle the resulting `CheckViolation` in Python gracefully
2. Implement a search command that finds all books currently borrowed by a specific member using a JOIN query
3. Add a `UNIQUE` constraint on `(book_id, member_id)` where `returned_at IS NULL` (a partial unique index) — so the same member cannot borrow the same book twice simultaneously

