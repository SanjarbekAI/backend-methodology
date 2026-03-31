# L08 Tasks — Sets & Dictionaries

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The duplicate cleaner

**Scenario**
A marketing platform collected email addresses from three different campaigns, but the lists contain many duplicates. The system needs to merge all three lists and output a clean list of unique emails only.

**Your task**
- Define three lists:
  ```python
  campaign_a = ["ali@mail.com", "sara@mail.com", "bob@mail.com", "ali@mail.com"]
  campaign_b = ["sara@mail.com", "layla@mail.com", "nodira@mail.com"]
  campaign_c = ["bob@mail.com", "layla@mail.com", "kamol@mail.com", "sara@mail.com"]
  ```
- Combine all three into one set (no duplicates)
- Convert the result back to a sorted list
- Print the unique emails and the total count

**Expected output**
```
Unique emails: ['ali@mail.com', 'bob@mail.com', 'kamol@mail.com', 'layla@mail.com', 'nodira@mail.com', 'sara@mail.com']
Total unique: 6
```

**File:** `task_01.py`

---

## Task 2 — The student registry

**Scenario**
A university admission office stores each student's data in a dictionary. The system must display a formatted profile, update the GPA, add a new field, and safely retrieve a field that might not exist.

**Your task**
- Create a student dictionary with: `id`, `name`, `faculty`, `year`, `gpa`
- Print all fields in a formatted profile card
- Update the GPA to a new value
- Add a new field: `email`
- Use `.get()` to safely retrieve `phone` (which doesn't exist) — show `"Not provided"` as the default
- Print the updated profile

**Expected output**
```
=== Student Profile ===
ID:      S-10423
Name:    Kamola Yusupova
Faculty: Computer Science
Year:    2
GPA:     3.75

=== Updated Profile ===
GPA:     3.90
Email:   kamola@uni.edu
Phone:   Not provided
```

**File:** `task_02.py`

---

## Task 3 — The product catalog lookup

**Scenario**
An online store has a product catalog stored as a dictionary. A checkout system looks up each item in the cart to retrieve the price, and handles missing items gracefully.

**Your task**
- Define a catalog:
  ```python
  catalog = {
      "laptop": 8500000,
      "mouse": 120000,
      "keyboard": 350000,
      "monitor": 2400000,
      "webcam": 580000
  }
  ```
- Define a cart: `cart = ["laptop", "mouse", "tablet", "keyboard"]`
- For each item in the cart, look up the price using `.get()` — if not found, print "Item not found"
- Calculate and print the total for found items only

**Expected output**
```
laptop:   8,500,000 sum
mouse:      120,000 sum
tablet:   Item not found
keyboard:   350,000 sum
---------------------
Total:    8,970,000 sum
```

**File:** `task_03.py`

---

## Task 4 — The permission checker

**Scenario**
A software platform assigns permissions to users. The system needs to compare a user's permissions against the required permissions for a specific action — using set operations to determine what is missing and what is already granted.

**Your task**
- Define:
  ```python
  user_permissions = {"read", "write", "comment"}
  required_permissions = {"read", "write", "delete", "admin"}
  ```
- Find which permissions the user already has (intersection)
- Find which permissions the user is missing (difference: required - user)
- Find all unique permissions across both sets (union)
- Print whether the user has full access (all required permissions granted)

**Expected output**
```
Granted:   {'read', 'write'}
Missing:   {'delete', 'admin'}
All perms: {'read', 'write', 'comment', 'delete', 'admin'}
Full access: False
```

**File:** `task_04.py`

---

## Task 5 — The nested employee database

**Scenario**
A company's HR system stores each employee's full record in a nested dictionary. The system needs to display all employees, give one a promotion (salary raise + title update), and find the highest earner.

**Your task**
- Create a nested dictionary with 3 employees. Each has: `name`, `department`, `title`, `salary`
- Print all employees in a formatted table
- Give the employee with ID "E002" a 15% salary raise and update their title to "Senior " + current title
- Find and print the name and salary of the highest earner

**Expected output**
```
ID    Name              Department     Title              Salary
E001  Rustam Nazarov    Engineering    Developer          7,500,000
E002  Sara Yusupova     Design         Designer           5,200,000
E003  Kamol Toshmatov   Marketing      Manager            6,800,000

After promotion:
E002  Sara Yusupova     Design         Senior Designer    5,980,000

Highest earner: Rustam Nazarov — 7,500,000 sum
```

**File:** `task_05.py`

---

## Task 6 — The word frequency counter

**Scenario**
A content analysis tool reads a sentence and counts how many times each word appears. Marketing teams use this to find the most repeated keywords in customer reviews.

**Your task**
- Define: `text = "the quick brown fox jumps over the lazy dog the fox"`
- Split the text into words
- Use a dictionary to count how many times each word appears (loop through the words)
- Print each word and its count, sorted alphabetically
- Print the most frequent word and its count

**Expected output**
```
brown: 1
dog:   1
fox:   2
jumps: 1
lazy:  1
over:  1
quick: 1
the:   3

Most frequent: "the" — 3 times
```

**File:** `task_06.py`

