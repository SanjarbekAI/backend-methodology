# L22 Tasks — Practice: Intermediate Review

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The contacts & notes manager (main project)

**Scenario**
A developer wants a personal contacts and notes manager they can run from the terminal. It ties together every Month 2 concept in a single cohesive application.

**Your task**
- Build the full contacts manager as described in `lesson.md`
- Code must be organized into at least `models.py`, `storage.py`, `main.py`
- Contacts and notes must be dataclasses with full type hints
- Phone and email must be validated with RegEx on entry
- All search/filter operations must use comprehensions
- ID generation must use a generator
- Data persists between runs via JSON

**Expected flow**
```
=== Contacts Manager ===
Loaded 4 contacts.

1. Add Contact       5. View Detail
2. View All          6. Delete Contact
3. Search            7. Exit
4. Add Note

> 3
Search query: ali
Results:
  C-0001  Ali Karimov    +998912345678   ali@mail.com   [work, friend]
  C-0003  Alisher Nazarov +998901234567  alisher@co.com [colleague]
```

**File:** `main.py` (+ `models.py`, `storage.py`)

---

## Task 2 — The regex & JSON data extractor

**Scenario**
A data engineer receives a mixed-format text report and must extract structured data from it using RegEx, then output the results as a clean JSON file for further processing.

**Your task**
- Define a multi-line text string containing:
  - At least 4 names in format `Name: Firstname Lastname`
  - At least 4 emails
  - At least 4 phone numbers in various formats
  - At least 2 dates in various formats (`DD/MM/YYYY`, `YYYY-MM-DD`, etc.)
- Use RegEx to extract all of each type
- Normalize phones to digits-only using `re.sub()`
- Build a list of contact dicts combining the extracted data
- Save to `extracted_contacts.json` with `indent=2`
- Print extraction summary

**Expected output**
```
Extracted:
  Names:  4
  Emails: 4
  Phones: 4
  Dates:  2

Saved to extracted_contacts.json ✓

Preview:
{
  "name": "Ali Karimov",
  "email": "ali@mail.com",
  "phone": "998912345678"
}
```

**File:** `task_02.py`

