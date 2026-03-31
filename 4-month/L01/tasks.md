# L34 Tasks — Git Fundamentals & Terminal Basics

Complete the tasks below. Create the required files and folders for each task as instructed.

---

## Task 1 — Terminal navigation — the file explorer

**Scenario**
Amir just started at a software company. His team lead tells him: "All our project folders live in `~/projects`. Go in, look around, and find the config file." Amir has never used a terminal before. He needs to navigate, list, and read files without touching a mouse.

**Your task**
- Open your terminal (Git Bash on Windows, Terminal on macOS/Linux)
- Run `pwd` and write down what it prints
- Run `ls -la` — identify at least one hidden file or folder (starts with `.`)
- Create this folder structure using only terminal commands:
  ```
  ~/projects/
    coffee-shop/
      menu.txt
      orders.txt
    inventory/
      stock.txt
  ```
- Write a few lines into `menu.txt` using `echo "Espresso - 15000" >> menu.txt`
- Print the contents of `menu.txt` using `cat`
- Move `stock.txt` into `coffee-shop/` folder
- Delete the now-empty `inventory/` folder

**Expected output**
```
# After cat menu.txt:
Espresso - 15000
Cappuccino - 18000
Latte - 20000

# After ls coffee-shop/:
menu.txt  orders.txt  stock.txt
```

**File:** No `.py` file — screenshot or terminal session log is your submission.

---

## Task 2 — First repository — a Python project

**Scenario**
Nilufar is a junior developer who just wrote a small Python script that calculates monthly electricity bills. Her manager says: "Before you share it, put it in Git — we need version history for all scripts."

**Your task**
- Create a folder called `electricity-bill/`
- Inside it, write a Python script `bill.py` that:
  - Asks the user for `units_used` (float)
  - Calculates the bill: first 100 units at 400 sum/unit, next 200 at 650 sum/unit, above 300 at 900 sum/unit
  - Prints a formatted invoice with the total
- Initialize a Git repository in that folder
- Run `git status` and observe which files appear
- Stage and commit `bill.py` with a meaningful commit message
- Add a `README.md` explaining what the script does
- Make a second commit for the README
- Run `git log --oneline` and show both commits

**Expected output**
```
$ git log --oneline
a3f9c12 Add README with project description
e1b8f44 Add electricity bill calculator script

$ python bill.py
Enter units used this month: 350
--- Invoice ---
First 100 units:  40,000 sum
Next 200 units:  130,000 sum
Remaining 50 units: 45,000 sum
Total: 215,000 sum
```

**File:** `task_02/bill.py`

---

## Task 3 — Staging area deep dive

**Scenario**
Bekzod is building a pharmacy stock manager. He has been editing three files simultaneously. He wants to commit only the drug search feature today and leave the billing changes for tomorrow — they're not tested yet.

**Your task**
- Create a project folder `pharmacy/` with three files:
  - `search.py` — a function `find_drug(name, stock_dict)` that returns drug info or `"Not found"`
  - `billing.py` — a placeholder function `calculate_bill()` that just has `pass`
  - `config.py` — a dict with `{"currency": "UZS", "tax_rate": 0.12}`
- Initialize Git, make an initial commit with all three files
- Now add real logic to `search.py` (make it actually work)
- Also edit `billing.py` (add some partial, broken logic)
- Run `git status` — observe both files are modified
- Stage ONLY `search.py`
- Run `git diff --staged` — confirm only search changes are shown
- Commit ONLY `search.py` with message `"Implement drug search by name"`
- Run `git log --oneline` — show the two commits
- Run `git status` — show `billing.py` is still modified but uncommitted

**Expected output**
```
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   search.py

Changes not staged for commit:
        modified:   billing.py

$ git log --oneline
7d3e991 Implement drug search by name
1a2b3c4 Initial commit: add pharmacy project files
```

**File:** `task_03/search.py`

---

## Task 4 — Commit message discipline

**Scenario**
Zarina is a code reviewer at a fintech startup. She opens the Git history of the payment module and sees commits labeled `"fix"`, `"update"`, `"asdf"`, `"changes2"`. She sends an angry Slack message: "Who wrote these? I can't understand what happened for the last two weeks!"

**Your task**
- Create a file `payment.py` with a `Payment` class that has: `amount`, `currency`, `status` attributes and a `process()` method that prints a confirmation message
- Make **5 separate commits** as you build it step by step:
  1. Add empty `Payment` class with `__init__`
  2. Add `process()` method that prints confirmation
  3. Add currency validation (only accept `"UZS"`, `"USD"`, `"EUR"`)
  4. Add status tracking (`"pending"` → `"completed"` after process)
  5. Add `__repr__` for readable printing
- Each commit message must follow the format: `"verb: short description"` — e.g., `"Add: Payment class skeleton"`, `"Add: process() method with confirmation"`, `"Validate: currency must be UZS, USD, or EUR"`
- Run `git log --oneline` at the end and show all 5 commits

**Expected output**
```
$ git log --oneline
9f1c2d3 Add: __repr__ for readable Payment output
8e2b1a4 Track: status changes from pending to completed
7d3c9f2 Validate: currency must be UZS USD or EUR
6c2b8e1 Add: process() method with confirmation message
5b1a7d0 Add: Payment class skeleton with __init__
```

**File:** `task_04/payment.py`

---

## Task 5 — The .gitignore guardian

**Scenario**
Jamshid accidentally pushed his `.env` file (containing his database password) to GitHub. His tech lead called him immediately. "We need to rotate all credentials now," she said. This happens to thousands of developers every year. Jamshid needs to learn `.gitignore` the right way — before it's too late.

**Your task**
- Create a project folder `secure-app/`
- Create these files:
  - `app.py` — a simple script that prints `"App running. Config loaded."`
  - `.env` — add fake credentials: `DB_PASSWORD=super_secret_123` and `API_KEY=abc-xyz-999`
  - `requirements.txt` — add `psycopg2-binary` and `python-dotenv`
  - `logs/app.log` — add some fake log lines
- Create a proper `.gitignore` that excludes: `.env`, `logs/`, `__pycache__/`, `*.pyc`, `venv/`
- Initialize Git and run `git status` — confirm `.env` and `logs/` do NOT appear
- Stage and commit only `app.py`, `requirements.txt`, and `.gitignore`
- Run `git status` to confirm clean state
- BONUS: try `git add .env` and observe what Git says

**Expected output**
```
$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        app.py
        requirements.txt

# .env and logs/ do not appear — they are ignored

$ git log --oneline
3c1d9e8 Add app skeleton with gitignore protecting secrets
```

**File:** `task_05/app.py`

