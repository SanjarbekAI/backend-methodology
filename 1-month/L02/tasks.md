# L02 Tasks — Variables & Data Types

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The student profile

**Scenario**
A university's registration system needs to store and display a student's basic profile when they first enroll. The system prints a formatted summary card for the admissions office.

**Your task**
- Create variables for: student name (str), age (int), GPA (float), is_enrolled (bool)
- Print each variable on its own labelled line
- Print the type of each variable using `type()`

**Expected output**
```
Name: Kamola Yusupova
Age: 19
GPA: 3.75
Enrolled: True

Types:
Name type: <class 'str'>
Age type: <class 'int'>
GPA type: <class 'float'>
Enrolled type: <class 'bool'>
```

**File:** `task_01.py`

---

## Task 2 — The product listing

**Scenario**
An e-commerce platform needs to store product details for each item in its catalog. A script generates a display card for each product in the warehouse dashboard.

**Your task**
- Create variables for: product name, SKU code (a short ID like "AB-1042"), price, stock count, is_available
- Print a formatted product card showing all five values
- Use appropriate data types for each variable (think carefully about which type fits each one)

**Expected output**
```
========== PRODUCT CARD ==========
Product:    Wireless Headphones
SKU:        AB-1042
Price:      49.99 USD
Stock:      134 units
Available:  True
==================================
```

**File:** `task_02.py`

---

## Task 3 — The type detective

**Scenario**
A junior developer at a data company received a script from a client but the variable types were all mixed up. The developer must investigate each variable, print its current value and type, then explain what the correct type *should* be.

**Your task**
- Create these 6 variables exactly as shown:
  ```
  order_id = "10045"
  quantity = "3"
  discount = True
  is_premium = 1
  rating = "4.8"
  username = 99
  ```
- For each variable, print: the value and its current type using `type()`
- After printing all, add a comment next to each variable explaining whether the type is correct or what it should be changed to

**Expected output**
```
order_id: 10045 → <class 'str'>
quantity: 3 → <class 'str'>
discount: True → <class 'bool'>
is_premium: 1 → <class 'int'>
rating: 4.8 → <class 'str'>
username: 99 → <class 'int'>
```

**File:** `task_03.py`

---

## Task 4 — The swap trick

**Scenario**
A logistics company tracks two delivery trucks. Midway through the day, the system needs to swap the assigned routes of Truck A and Truck B without losing either route value.

**Your task**
- Create two variables: `truck_a_route = "Route 7 — North District"` and `truck_b_route = "Route 12 — South District"`
- Print the routes before the swap
- Swap the values of the two variables (do NOT just reassign them manually — use Python's multiple assignment swap)
- Print the routes after the swap

**Expected output**
```
Before swap:
Truck A: Route 7 — North District
Truck B: Route 12 — South District

After swap:
Truck A: Route 12 — South District
Truck B: Route 7 — North District
```

**File:** `task_04.py`

---

## Task 5 — The dynamic type experiment

**Scenario**
A developer is explaining dynamic typing to a new intern at a tech company. They build a small demonstration script that shows how a single variable can change its type multiple times and how `type()` tracks it.

**Your task**
- Create one variable called `data`
- Assign it an integer, print the value and type
- Reassign it to a float, print the value and type
- Reassign it to a string, print the value and type
- Reassign it to a boolean, print the value and type
- Add inline comments explaining what is happening at each step

**Expected output**
```
data = 100 → type: <class 'int'>
data = 3.14 → type: <class 'float'>
data = hello → type: <class 'str'>
data = True → type: <class 'bool'>
```

**File:** `task_05.py`

---

## Task 6 — The profile updater

**Scenario**
A fitness app stores user profile data. When a user updates their profile, the app must display the old values, apply the updates, and then display the new values.

**Your task**
- Create an initial profile: name, weight_kg (float), age (int), is_premium (bool)
- Print the full profile labelled as "Current profile"
- Update the weight and flip is_premium to the opposite value
- Print the updated profile labelled as "Updated profile"
- The printed output must clearly show what changed

**Expected output**
```
--- Current profile ---
Name: Rustam Nazarov
Weight: 82.5 kg
Age: 28
Premium member: False

--- Updated profile ---
Name: Rustam Nazarov
Weight: 79.0 kg
Age: 28
Premium member: True
```

**File:** `task_06.py`

