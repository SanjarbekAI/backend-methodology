# L11 — Practice: Basics

## Project brief
You are building a **command-line personal finance tracker** for a small household. The app lets a user record their daily income and expenses, view a summary, and save their records to a file so nothing is lost when the program closes. This is a real tool that someone could actually use every day.

---

## Requirements

1. Display a menu with options: Add Income, Add Expense, View Summary, View History, Save & Exit
2. Accept user input for each transaction: description and amount
3. Store transactions in a list of dictionaries (each with `type`, `description`, `amount`)
4. Calculate and display total income, total expenses, and current balance
5. Handle invalid inputs (non-numeric amounts, empty descriptions) with clear error messages
6. Save all transactions to `transactions.txt` when the user chooses Save & Exit
7. Load existing transactions from `transactions.txt` on startup (if the file exists)
8. Display transaction history as a formatted table

---

## Milestones

**Milestone 1 (0:00–0:30) — Core data & menu**
- Set up the `transactions` list
- Write the menu display and `while True` input loop
- Implement `Add Income` and `Add Expense` options with input validation

**Milestone 2 (0:30–1:00) — Summary & history**
- Implement `View Summary`: calculate income, expenses, balance
- Implement `View History`: print a formatted table of all transactions
- Add color-coded labels (+ for income, - for expense) using simple string prefixes

**Milestone 3 (1:00–1:30) — File I/O**
- Implement `Save & Exit`: write all transactions to `transactions.txt`
- Implement startup loading: read `transactions.txt` on launch if it exists
- Handle `FileNotFoundError` gracefully on first run

**Milestone 4 (1:30–2:00) — Polish & edge cases**
- Handle empty transaction list in history and summary
- Add input validation for amounts ≤ 0
- Add a transaction counter to the history display
- Test the full flow end-to-end: add → view → save → reopen → view loaded data

---

## Bonus challenges

1. **Filter view:** Add a menu option to view only income transactions or only expense transactions.
2. **Monthly limit:** Let the user set a monthly expense budget and warn them when they exceed it.
3. **CSV export:** Instead of plain text, save to a `.csv` file so it can be opened in Excel.

