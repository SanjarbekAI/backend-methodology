# L10 Tasks — File I/O & Modules Intro

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The daily log writer

**Scenario**
A delivery company's dispatch system logs every completed delivery to a daily log file. Each log entry contains the time, driver name, and delivery address. New entries must be added without erasing previous ones.

**Your task**
- Import `datetime`
- Define 3 delivery records as strings (driver name + address)
- Open `deliveries_log.txt` in append mode and write each record with today's date prepended
- After writing, open the file in read mode and print all its contents
- Use `with` for both operations

**Expected output** (printed to screen)
```
[2026-03-30] Driver: Rustam — 14 Amir Temur St, Tashkent
[2026-03-30] Driver: Layla — 7 Navoi Ave, Tashkent
[2026-03-30] Driver: Bobur — 22 Mustaqillik Sq, Tashkent
```

**File:** `task_01.py`

---

## Task 2 — The config file reader

**Scenario**
A web application loads its settings from a plain text config file at startup. Each line contains a key-value pair in the format `KEY=VALUE`. The app reads the file and stores the settings in a dictionary.

**Your task**
- First, create a file called `config.txt` with these lines:
  ```
  APP_NAME=MyShop
  VERSION=2.1
  DEBUG=True
  MAX_USERS=500
  ```
- Write a script that reads `config.txt` line by line
- For each line, split on `=` to get the key and value
- Store all settings in a dictionary
- Print the dictionary and then print the value of `APP_NAME` and `MAX_USERS` specifically

**Expected output**
```
Config loaded: {'APP_NAME': 'MyShop', 'VERSION': '2.1', 'DEBUG': 'True', 'MAX_USERS': '500'}
App name:  MyShop
Max users: 500
```

**File:** `task_02.py`

---

## Task 3 — The student records saver

**Scenario**
A school's administration tool collects student names and scores from the user and saves them to a text file, one per line. The file can be read back later for a printed report.

**Your task**
- Ask the user to enter 3 student names and their scores (use `input()`)
- Save each record to `students.txt` in format: `Name: {name}, Score: {score}`
- After saving, read the file back and print a formatted report
- Handle `ValueError` if a non-numeric score is entered (re-ask)

**Expected output**
```
Enter student 1 name: Kamola
Enter student 1 score: 88
Enter student 2 name: Rustam
Enter student 2 score: 74
Enter student 3 name: Sara
Enter student 3 score: 91

=== Student Report ===
Name: Kamola, Score: 88
Name: Rustam, Score: 74
Name: Sara, Score: 91
```

**File:** `task_03.py`

---

## Task 4 — The dice simulator

**Scenario**
A board game app simulates dice rolls for 4 players. Each player rolls two dice and their total score is recorded. The app uses Python's `random` module and saves the results to a file.

**Your task**
- Import `random`
- Define 4 player names
- For each player, simulate rolling two dice (1–6 each) using `random.randint()`
- Print each player's roll and total
- Save all results to `dice_results.txt`
- Print the winner (highest total — handle ties)

**Expected output**
```
Rustam:  🎲 4 + 🎲 6 = 10
Layla:   🎲 3 + 🎲 3 = 6
Kamola:  🎲 6 + 🎲 5 = 11
Bobur:   🎲 2 + 🎲 4 = 6

Winner: Kamola with 11 points!
Results saved to dice_results.txt
```

**File:** `task_04.py`

---

## Task 5 — The file backup tool

**Scenario**
A developer's tool makes a backup copy of a text file before editing it. The tool checks if the original file exists, copies its content to a backup file, then writes new content to the original.

**Your task**
- Import `os`
- Check if `original.txt` exists using `os.path.exists()`
- If it does NOT exist, create it with 3 lines of sample text
- Read the content and write it to `original_backup.txt`
- Overwrite `original.txt` with new content (3 different lines)
- Print a confirmation message showing original and backup file contents

**Expected output**
```
original.txt did not exist — created with sample content.
Backup created: original_backup.txt
original.txt updated with new content.

--- Backup content ---
Line 1: Original data
Line 2: More original data
Line 3: Even more data

--- New content ---
Line 1: Updated data
Line 2: Fresh content
Line 3: New entry
```

**File:** `task_05.py`

---

## Task 6 — The word count analyzer

**Scenario**
A publishing tool analyzes a text file to count the total number of words, lines, and unique words. Editors use this to measure document complexity and check for keyword repetition.

**Your task**
- Create a file called `article.txt` with at least 5 lines of any text (can be made up)
- Read the file and calculate:
  - Total number of lines
  - Total number of words
  - Number of unique words (use a set)
  - The 3 most common words (use a dictionary to count, then sort)
- Print all statistics

**Expected output**
```
=== Article Analysis ===
Lines:        5
Total words:  47
Unique words: 38
Repetition:   19.1%

Top 3 words:
  "the" — 5 times
  "and" — 3 times
  "in"  — 2 times
```

**File:** `task_06.py`

