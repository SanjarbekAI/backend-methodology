# L23 Tasks — OOP: Classes & Objects

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The product catalog item

**Scenario**
An e-commerce platform models each product as an object. The product tracks its own price history and can apply discounts, restock, and generate a display card.

**Your task**
- Create a `Product` class with `__init__`: `sku`, `name`, `price`, `stock`, `category`
- Add methods: `apply_discount(percent)`, `restock(qty)`, `sell(qty)` (returns False if insufficient stock), `display_card()` (prints formatted card)
- Track a class variable `total_products` that increments on each instantiation
- Create 3 products, perform operations on each, print display cards

**Expected output**
```
========== PRODUCT ==========
SKU:      ELEC-0042
Name:     Wireless Headphones
Price:    297,500 sum  (was 350,000)
Stock:    15 units
Category: Electronics
=============================
Total products in catalog: 3
```

**File:** `task_01.py`

---

## Task 2 — The student record

**Scenario**
A university's academic system models each student as an object that stores their courses and grades, calculates GPA, and generates a transcript.

**Your task**
- Create a `Student` class: `student_id`, `name`, `faculty`, `year`
- Instance variable `grades: dict[str, float]` initialized as empty dict in `__init__`
- Methods: `add_grade(course, score)`, `get_gpa() -> float` (average of all grades), `get_transcript() -> str` (formatted multi-line string)
- Create 2 students, add 4 grades each, print transcripts

**Expected output**
```
=== TRANSCRIPT ===
ID:      S-10421
Name:    Kamola Yusupova
Faculty: Computer Science
Year:    2

Course              Score
Mathematics         88.0
Algorithms          92.0
Database Systems    76.0
English             84.0

GPA: 3.40
```

**File:** `task_02.py`

---

## Task 3 — The library book tracker

**Scenario**
A library system models books as objects. Each book tracks whether it is available, who has borrowed it, and its borrow history.

**Your task**
- Create a `Book` class: `isbn`, `title`, `author`, `year`
- Instance variables: `is_available = True`, `borrower = None`, `borrow_count = 0`
- Class variable: `library_name = "Central Library"`
- Methods: `borrow(borrower_name) -> bool`, `return_book() -> None`, `info() -> str`
- Create 4 books, simulate borrowing and returning, print info for each

**Expected output**
```
[Central Library]
Title:     The Pragmatic Programmer
Author:    David Thomas, Andrew Hunt
ISBN:      978-0135957059
Status:    Borrowed by Rustam Nazarov
Borrows:   1
```

**File:** `task_03.py`

---

## Task 4 — The bank account system

**Scenario**
A fintech startup models bank accounts as objects. Each account encapsulates its balance and transaction history, enforcing rules on deposits and withdrawals.

**Your task**
- Create a `BankAccount` class: `account_id`, `owner`, `balance`
- Methods: `deposit(amount)`, `withdraw(amount) -> bool`, `transfer(other_account, amount) -> bool`, `get_statement() -> str`
- All amounts must be positive; withdrawals must not exceed balance
- Each successful transaction is recorded in `_history: list[str]`
- Create 2 accounts, perform deposits, withdrawal, a transfer, and print statements

**Expected output**
```
=== Statement: ACC-001 (Rustam) ===
Deposit:    +1,000,000
Deposit:    +500,000
Withdrawal: -200,000
Transfer→ACC-002: -300,000
Balance:    1,000,000 sum
```

**File:** `task_04.py`

---

## Task 5 — The employee roster

**Scenario**
An HR system models employees as objects and maintains a shared company roster. The class tracks all created employees at the class level and provides methods to search and report.

**Your task**
- Create an `Employee` class: `emp_id`, `name`, `department`, `salary`
- Class variable `_roster: list` that stores all created employees
- Class method `get_all() -> list` (returns all employees)
- Class method `find_by_department(dept: str) -> list`
- Class method `highest_earner() -> Employee`
- Instance method `give_raise(percent: float) -> None`
- Create 5 employees, give one a raise, then call all 3 class methods and print results

**Expected output**
```
All employees: 5
Engineering dept: ['Rustam Nazarov', 'Bobur Toshmatov']
Highest earner: Sara Yusupova — 9,200,000 sum (after raise)
```

**File:** `task_05.py`

