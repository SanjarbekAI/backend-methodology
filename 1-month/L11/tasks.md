# L11 Tasks — Practice: Basics

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The personal finance tracker (main project)

**Scenario**
A household wants a simple command-line tool to track daily income and expenses. The tool must survive a restart — data is saved to a file and reloaded automatically.

**Your task**
- Build the full finance tracker as described in `lesson.md`
- The app must have a working menu loop
- Implement all 5 menu options: Add Income, Add Expense, View Summary, View History, Save & Exit
- Transactions must persist between runs (saved to and loaded from `transactions.txt`)
- All invalid inputs must be caught with friendly error messages

**Expected flow**
```
=== Personal Finance Tracker ===
Loaded 3 existing transactions.

1. Add Income
2. Add Expense
3. View Summary
4. View History
5. Save & Exit

Choose option: 3

=== Summary ===
Total Income:   1,500,000 sum
Total Expenses:   380,000 sum
Balance:        1,120,000 sum
```

**File:** `task_01.py`

---

## Task 2 — The mini quiz game

**Scenario**
A language learning app includes a mini vocabulary quiz. The app asks 5 questions, tracks the score, handles wrong answer types gracefully, and saves the final score to a results file.

**Your task**
- Define 5 questions as a list of dictionaries: `{"question": "...", "answer": "..."}`
- Loop through each question, ask the user, check the answer (case-insensitive)
- Track score and print feedback after each answer
- At the end, print the final score and a performance message
- Save the result summary to `quiz_results.txt` (append mode — keeps history of attempts)
- Import `datetime` to stamp each quiz attempt with the date

**Expected output**
```
=== Vocabulary Quiz ===

Q1: What is the Uzbek word for "apple"?
Your answer: olma
✅ Correct!

Q2: What is the Uzbek word for "school"?
Your answer: maktab
✅ Correct!

...

=== Quiz Complete ===
Score: 4/5
Result: Good job! Keep practicing.
Saved to quiz_results.txt
```

**File:** `task_02.py`

