# L22 — Practice: Intermediate Review

## Project brief
You are building a **personal contacts and notes manager** — a CLI application that manages contacts (name, phone, email, tags) and attached notes. This project reviews the entire Month 2 curriculum: functions, modules, RegEx, JSON, type hints, and dataclasses — all working together as a coherent system.

---

## Requirements

1. Model `Contact` and `Note` as **dataclasses** with full type annotations
2. Validate phone numbers and emails using **RegEx** on input
3. Organize code into at least 2 modules: `models.py` (dataclasses) and `storage.py` (JSON I/O)
4. All data persists in `contacts.json` and loads on startup
5. Support menu operations: Add Contact, View All, Search by Name/Tag, Add Note to Contact, View Contact Detail, Delete Contact, Exit
6. Use **comprehensions** for all search and filter operations
7. Use a **generator** to create contact IDs
8. Use a **decorator** for input validation (re-asks if invalid)

---

## Milestones

**Milestone 1 (0:00–0:30) — Models & validation**
- Define `Contact` and `Note` dataclasses in `models.py`
- Write RegEx validators for phone and email
- Write the `__post_init__` validation logic

**Milestone 2 (0:30–1:00) — Storage layer**
- Write `save_contacts` and `load_contacts` in `storage.py`
- Handle the dataclass → dict → JSON and JSON → dict → dataclass conversion
- Test saving and loading independently

**Milestone 3 (1:00–1:30) — Search & display**
- Implement search by name (partial match, case-insensitive) using comprehensions
- Implement filter by tag using a set intersection
- Build the contact detail display including notes

**Milestone 4 (1:30–2:00) — CLI integration**
- Wire everything into `main.py` with the full menu loop
- Add the `if __name__ == "__main__":` guard
- Test end-to-end: create contacts, add notes, search, delete, save, reload

---

## Bonus challenges

1. **Export to CSV:** Add an export option that writes all contacts to a `.csv` file using Python's `csv` module.
2. **Tag statistics:** Show how many contacts have each tag, sorted by frequency (use dict comprehension + sorted with lambda).
3. **Duplicate detection:** On adding a new contact, warn if a contact with the same phone already exists.

