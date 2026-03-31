# L07 Tasks — Lists & Tuples

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The shopping cart manager

**Scenario**
An e-commerce website needs a script to simulate a shopping cart session. The cart starts empty, items are added, one is removed by name, and the final cart is displayed with a total item count.

**Your task**
- Start with an empty cart: `cart = []`
- Add these 5 products one by one using `.append()`: "Laptop", "Mouse", "Keyboard", "Webcam", "Monitor"
- Print the cart after all items are added
- Remove "Webcam" from the cart using `.remove()`
- Add "USB Hub" at position 2 using `.insert()`
- Print the final cart and the total number of items

**Expected output**
```
After adding items: ['Laptop', 'Mouse', 'Keyboard', 'Webcam', 'Monitor']
After changes:      ['Laptop', 'Mouse', 'USB Hub', 'Keyboard', 'Monitor']
Total items:        5
```

**File:** `task_01.py`

---

## Task 2 — The class gradebook

**Scenario**
A teacher's gradebook application stores student scores and needs to calculate the class average, find the highest and lowest scores, and display a sorted leaderboard.

**Your task**
- Define: `scores = [88, 72, 95, 61, 83, 90, 55, 77, 68, 84]`
- Calculate and print: total score, average (rounded to 1 decimal), highest score, lowest score
- Print a sorted leaderboard (highest to lowest) using `sorted()` with `reverse=True`
- Do NOT modify the original `scores` list

**Expected output**
```
Scores:    [88, 72, 95, 61, 83, 90, 55, 77, 68, 84]
Total:     773
Average:   77.3
Highest:   95
Lowest:    55
Leaderboard: [95, 90, 88, 84, 83, 77, 72, 68, 61, 55]
```

**File:** `task_02.py`

---

## Task 3 — The top-3 extractor

**Scenario**
A sales reporting system receives monthly revenue figures for 12 months and needs to extract the best quarter (top 3 months) and the most recent 3 months for a performance summary.

**Your task**
- Define: `monthly_revenue = [42000, 38000, 51000, 47000, 60000, 55000, 49000, 53000, 61000, 44000, 58000, 67000]`
- Use slicing to get: first 3 months, last 3 months
- Use `sorted()` to find the top 3 highest revenue months
- Print all three groups clearly

**Expected output**
```
First quarter:  [42000, 38000, 51000]
Last 3 months:  [44000, 58000, 67000]
Top 3 months:   [67000, 61000, 60000]
```

**File:** `task_03.py`

---

## Task 4 — The coordinates logger

**Scenario**
A delivery tracking system stores GPS waypoints as tuples (latitude, longitude). The system logs each delivery stop and calculates how many stops were made.

**Your task**
- Create 4 waypoints as tuples:
  ```python
  stop1 = (41.2995, 69.2401)   # Tashkent
  stop2 = (39.6542, 66.9597)   # Samarkand
  stop3 = (40.1000, 67.8400)   # Jizzakh
  stop4 = (40.3775, 71.7906)   # Andijan
  ```
- Unpack each tuple into `lat` and `lon` and print a formatted log entry
- Store all stops in a list called `route`
- Print the total number of stops

**Expected output**
```
Stop 1 → Lat: 41.2995, Lon: 69.2401
Stop 2 → Lat: 39.6542, Lon: 66.9597
Stop 3 → Lat: 40.1000, Lon: 67.8400
Stop 4 → Lat: 40.3775, Lon: 71.7906
Total stops: 4
```

**File:** `task_04.py`

---

## Task 5 — The inventory restacker

**Scenario**
A pharmacy inventory system needs to reorder its medicine stock list. Items are currently stored oldest-first but must be displayed newest-first. The system also needs to check if a specific medicine is in stock.

**Your task**
- Define: `inventory = ["Paracetamol", "Ibuprofen", "Amoxicillin", "Vitamin C", "Aspirin"]`
- Reverse the list using slicing (not `.reverse()`) and store it in `reversed_inventory`
- Check if "Ibuprofen" is in the inventory (use `in`)
- Check if "Melatonin" is in the inventory
- Remove the last item from the original `inventory` using `.pop()` and print what was removed

**Expected output**
```
Original:   ['Paracetamol', 'Ibuprofen', 'Amoxicillin', 'Vitamin C', 'Aspirin']
Reversed:   ['Aspirin', 'Vitamin C', 'Amoxicillin', 'Ibuprofen', 'Paracetamol']
Ibuprofen in stock: True
Melatonin in stock: False
Removed: Aspirin
```

**File:** `task_05.py`

---

## Task 6 — The leaderboard system

**Scenario**
A gaming platform needs to manage its live leaderboard. New players are inserted at the correct position, the bottom player is eliminated each round, and the top 3 players are announced at the end.

**Your task**
- Start with: `leaderboard = [9500, 8800, 7600, 6200, 5100]` (points, highest to lowest)
- Add a new score of `9000` — insert it in the correct sorted position (find where it belongs manually using a loop or by appending then sorting)
- Remove the lowest score using `.pop(-1)`
- Print the updated leaderboard
- Print the top 3 players using slicing

**Expected output**
```
After new entry:   [9500, 9000, 8800, 7600, 6200, 5100]
After elimination: [9500, 9000, 8800, 7600, 6200]
Top 3:             [9500, 9000, 8800]
```

**File:** `task_06.py`

