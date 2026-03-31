# L17 Tasks — Modules, Packages & Venv

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The math utilities module

**Scenario**
A data science team standardizes their helper functions into a shared math utilities module. Any team member can import it instead of rewriting the same calculations.

**Your task**
- Create `math_utils.py` with functions: `add`, `subtract`, `multiply`, `divide` (handle division by zero), `percentage(part, total)`, and a constant `TAX_RATE = 0.12`
- Create `task_01.py` that imports `math_utils` and:
  - Performs all 4 operations on two numbers of your choice
  - Calculates percentage for a test value
  - Uses `TAX_RATE` to compute tax on a price
  - Print all results clearly

**Expected output**
```
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
15 out of 200 = 7.5%
Tax on 500,000: 60,000 sum
```

**File:** `task_01.py` + `math_utils.py`

---

## Task 2 — The string tools package

**Scenario**
A backend team builds a reusable utilities package for string processing across multiple microservices. It is structured as a proper Python package.

**Your task**
- Create a folder `string_tools/` with:
  - `__init__.py` (exports all functions)
  - `cleaner.py`: `strip_and_title(text)`, `remove_extra_spaces(text)`
  - `validator.py`: `is_valid_email(email)` (checks for `@` and `.`), `is_strong_password(pwd)` (length ≥ 8, has digit, has upper)
- Create `task_02.py` that imports from the package and tests all 4 functions with sample data

**Expected output**
```
"  hello world  " → "Hello World"
"too   many   spaces" → "too many spaces"
"ali@mail.com" is valid email: True
"badmail" is valid email: False
"Hello1234" is strong password: True
"weak" is strong password: False
```

**File:** `task_02.py` + `string_tools/` package

---

## Task 3 — The project bootstrapper

**Scenario**
A developer at a startup is setting up a new Python project from scratch. They need a script that prints a checklist of setup steps, including creating a venv, installing dependencies, and generating a starter `requirements.txt`.

**Your task**
- Create `task_03.py` with `if __name__ == "__main__":` guard
- Inside the guard: print a step-by-step setup guide with the exact commands for Windows and Mac/Linux
- Create a sample `requirements.txt` file programmatically using file I/O with 5 realistic packages and pinned versions
- Print confirmation that the file was created and show its contents

**Expected output**
```
=== Project Setup Guide ===

Step 1: Create virtual environment
  Windows: python -m venv .venv
  Mac/Linux: python3 -m venv .venv

Step 2: Activate virtual environment
  Windows: .venv\Scripts\Activate.ps1
  Mac/Linux: source .venv/bin/activate

Step 3: Install dependencies
  pip install -r requirements.txt

Step 4: Deactivate when done
  deactivate

requirements.txt created:
  requests==2.31.0
  flask==3.0.2
  python-dotenv==1.0.1
  sqlalchemy==2.0.28
  pydantic==2.6.4
```

**File:** `task_03.py`

---

## Task 4 — The requirements analyzer

**Scenario**
A DevOps engineer needs to audit a project's `requirements.txt` to count packages, identify any that are unpinned (no version specified), and group them alphabetically.

**Your task**
- Create a sample `requirements_sample.txt` with 8 packages (some pinned, some not)
- Write `task_04.py` that reads the file and:
  - Counts total packages
  - Lists pinned packages (contain `==`)
  - Lists unpinned packages (no version)
  - Prints a summary report

**Expected output**
```
=== Requirements Audit ===
Total packages: 8

Pinned (4):
  flask==3.0.2
  requests==2.31.0
  sqlalchemy==2.0.28
  pydantic==2.6.4

Unpinned (4) — WARNING: version not locked:
  numpy
  pandas
  matplotlib
  scikit-learn
```

**File:** `task_04.py`

---

## Task 5 — The module runner guard

**Scenario**
A developer is building a utility module called `converter.py` that will be imported by other scripts. They want to include a self-test that only runs when the file is executed directly, not when it is imported.

**Your task**
- Create `converter.py` with:
  - `celsius_to_fahrenheit(c)`, `km_to_miles(km)`, `usd_to_uzs(usd, rate=12600)`
  - A `if __name__ == "__main__":` block that runs 3 test conversions and prints them
- Create `task_05.py` that imports `converter` and uses all 3 functions with different values
- Verify that running `task_05.py` does NOT trigger the test block in `converter.py`

**Expected output** (when running task_05.py)
```
37°C = 98.6°F
42 km = 26.1 miles
150 USD = 1,890,000 UZS
```

*(The converter self-test block must NOT appear in this output.)*

**File:** `task_05.py` + `converter.py`

