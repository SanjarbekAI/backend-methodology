# L35 Tasks — Git Branching, Merging & Team Workflows

Complete the tasks below. Each task simulates a real team scenario. Follow the Git commands exactly and note the output at each step.

---

## Task 1 — Branch and merge — the clean path

**Scenario**
Sardor is a backend developer at a food delivery startup. He needs to add a "restaurant rating" feature to the API. His team rule is: never commit features directly to `main`. He must create a branch, build the feature, then merge it cleanly.

**Your task**
- Create a new project folder `food-delivery/` and initialize Git
- Create `main.py` with a `Restaurant` class that has `name` and `cuisine` attributes — commit this as the initial commit on `main`
- Create a branch called `feature/restaurant-rating`
- On that branch, add a `rating: float` attribute and a `set_rating(score)` method with validation (1.0–5.0 only) to the `Restaurant` class
- Commit on the feature branch with a good message
- Switch back to `main` — confirm the rating feature is NOT there yet
- Merge `feature/restaurant-rating` into `main`
- Confirm the feature is now in `main`
- Delete the feature branch
- Run `git log --oneline` to show the history

**Expected output**
```
$ git log --oneline
c4d2f91 Add: restaurant rating with validation (1.0-5.0)
a1b2c3d Initial commit: add Restaurant class

$ git branch
* main
# feature branch is gone

$ python main.py
Restaurant: Osh Markazi | Cuisine: Uzbek | Rating: 4.5
```

**File:** `task_01/main.py`

---

## Task 2 — Simulating a merge conflict

**Scenario**
Malika and Rustam both work on the same project. Malika is improving the price calculation method and Rustam is also changing the same function for a different reason. When they try to merge, Git cannot decide which version to keep.

**Your task**
- Create `shop/` folder, initialize Git, create `pricing.py` with a `calculate_total(price, qty)` function that returns `price * qty` — commit to `main`
- Create branch `malika/discount` — on this branch, change the function to apply a 10% discount: `return price * qty * 0.9`
- Commit on `malika/discount`
- Switch back to `main`, create branch `rustam/tax` — on this branch, change the same line to add 12% tax: `return price * qty * 1.12`
- Commit on `rustam/tax`
- Switch to `main`, merge `malika/discount` (clean merge)
- Now try to merge `rustam/tax` — observe the conflict
- Resolve the conflict manually: the correct final formula is `price * qty * 0.9 * 1.12` (discount first, then tax)
- Complete the merge with a commit message `"Merge: combine discount and tax calculation"`
- Run `git log --oneline --graph`

**Expected output**
```
$ git log --oneline --graph
*   9f2c1e8 Merge: combine discount and tax calculation
|\
| * 7d3b2a1 Add: 12% tax to total price
* | 5c2a1b9 Add: 10% loyalty discount
|/
* 3b1a0c8 Initial commit: add pricing function
```

**File:** `task_02/pricing.py`

---

## Task 3 — Remote workflow — push and pull

**Scenario**
Dilnoza just got her first job. On day one, her manager says: "Clone our repo, make your changes on a new branch, and push it — we'll review it in a Pull Request." She needs to complete the full push/pull cycle without breaking anything.

**Your task**
- Create a free GitHub account if you don't have one
- Create a new **public** repository on GitHub called `python-practice` (initialize with README)
- Clone it to your local machine using `git clone`
- Create a branch `feature/hello-script`
- Add a Python file `hello.py` that prints: `"Hello from [your name]! This is my first push to GitHub."`
- Commit and push the branch to GitHub: `git push -u origin feature/hello-script`
- Open GitHub in the browser — find your branch and verify the file is there
- Simulate a teammate's change: on GitHub's web UI, edit `README.md` directly (add one line)
- Back in terminal: `git fetch origin` then `git pull origin main`
- Run `git log --oneline` and show the README commit appears

**Expected output**
```
$ git log --oneline
f3e2d1c Update README with project description   ← from GitHub UI
a2b1c0d Add: hello script with personal greeting
b1c2d3e Initial commit
```

**File:** `task_03/hello.py`

---

## Task 4 — Feature branch workflow end-to-end

**Scenario**
Bobur is the only developer at a small clinic. He is building a patient management script and has learned from previous mistakes — he now uses the full feature branch workflow for every change, even working alone, because he knows it protects him from his own mistakes.

**Your task**
- Create `clinic/` project with `patients.py` containing an empty `PatientRegistry` class — initial commit on `main`
- For each of the following features, create a separate branch, implement it, commit, then merge back to `main`:
  - `feature/add-patient` → add `add_patient(name, age, diagnosis)` method that stores patient as a dict in a list
  - `feature/search-patient` → add `search_by_name(name)` method returning matching patients
  - `feature/report` → add `generate_report()` method printing all patients formatted
- After all 3 merges, `git log --oneline --graph` should show 3 merge points
- The final `patients.py` should have a working demo in `if __name__ == "__main__":` block

**Expected output**
```
$ git log --oneline --graph
*   d5e4f3a Merge: feature/report into main
|\
| * c4d3e2b Add: generate_report() with formatted output
|/
*   b3c2d1a Merge: feature/search-patient into main
|\
| * a2b1c0d Add: search_by_name() method
|/
*   f1e0d9c Merge: feature/add-patient into main
|\
| * e0f9e8d Add: add_patient() with dict storage
|/
* d9e8f7c Initial commit: add empty PatientRegistry
```

**File:** `task_04/patients.py`

---

## Task 5 — Stash and recover

**Scenario**
Kamron is halfway through writing a new data validation feature when his team lead messages: "Critical bug on main — the app is broken in production, fix it NOW." Kamron's current work is not ready to commit. He needs to drop everything, fix the bug on `main`, and come back to his feature later.

**Your task**
- Create `validator/` project with `validate.py` containing a `validate_email(email)` function that always returns `True` (placeholder) — commit to `main`
- Create branch `feature/regex-validation` and start editing `validate.py` with a real regex implementation (it doesn't need to be finished)
- WITHOUT committing, stash your work: `git stash`
- Run `git status` — confirm working directory is clean
- Switch to `main`, "fix the bug" by changing `return True` to `return bool(email and "@" in email)` — commit: `"Hotfix: basic email check before regex is ready"`
- Switch back to `feature/regex-validation`
- Run `git stash pop` — confirm your regex work is restored
- Finish the regex validation: use `re.match(r'^[\w.-]+@[\w.-]+\.\w{2,}$', email)`
- Commit the completed feature and merge into `main`

**Expected output**
```
$ git stash list
stash@{0}: WIP on feature/regex-validation: working on regex

$ git log --oneline
9c8b7a6 Add: full regex email validation
8b7a6f5 Hotfix: basic email check before regex is ready
7a6f5e4 Initial commit: add placeholder email validator
```

**File:** `task_05/validate.py`

