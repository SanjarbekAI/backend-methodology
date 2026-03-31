# L18 Tasks — Iterators, Dates & Math

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The subscription expiry checker

**Scenario**
A SaaS platform checks whether user subscriptions are still active, about to expire (within 7 days), or already expired. The billing team runs this check daily.

**Your task**
- Import `datetime` and `timedelta`
- Define 5 users with subscription end dates (as `datetime.date` objects — use dates relative to today: some past, some near, some future)
- For each user, determine their status: `"Active"`, `"Expiring soon"`, or `"Expired"`
- Print a formatted table with user name, expiry date, days remaining, and status

**Expected output**
```
Name           Expiry        Days Left   Status
Ali Karimov    2026-04-05    6           Expiring soon
Sara Yusupova  2026-05-10    41          Active
Bobur Nazarov  2026-03-20    -10         Expired
Layla Hassan   2026-04-02    3           Expiring soon
Rustam Toshev  2026-06-01    63          Active
```

**File:** `task_01.py`

---

## Task 2 — The age calculator

**Scenario**
A hospital's patient intake system calculates each patient's exact age in years, their next birthday, and how many days until that birthday — used for age-sensitive medication dosing.

**Your task**
- Import `datetime`
- Define 4 patient birth dates using `datetime.date(year, month, day)`
- For each patient:
  - Calculate current age in years
  - Find their next birthday this year (or next year if already passed)
  - Calculate days until next birthday
- Print a formatted patient card

**Expected output**
```
Patient: Kamola Yusupova
DOB:     1999-07-15
Age:     26 years
Next BD: 2026-07-15 (107 days away)
```

**File:** `task_02.py`

---

## Task 3 — The delivery scheduler

**Scenario**
An e-commerce platform calculates estimated delivery dates based on the shipping zone. Orders placed after 3 PM are processed the next business day. Weekends don't count as processing days.

**Your task**
- Import `datetime` and `timedelta`
- Define today's order placement time using `datetime.datetime.now()`
- If current hour ≥ 15, the processing starts tomorrow; otherwise today
- Add the correct number of business days (skip Saturday=5, Sunday=6) for each zone:
  - Local: +2 business days
  - National: +5 business days
  - International: +10 business days
- Print the estimated delivery date for each zone, formatted as `"Monday, April 6, 2026"`

**Expected output**
```
Order placed: 2026-03-30 16:42
Processing starts: 2026-03-31

Estimated delivery:
  Local:         Wednesday, April 02, 2026
  National:      Monday, April 07, 2026
  International: Thursday, April 16, 2026
```

**File:** `task_03.py`

---

## Task 4 — The circle geometry tool

**Scenario**
A construction company's measurement app calculates dimensions of circular structures — pipes, columns, and tanks. The tool uses the `math` module for precise geometric calculations.

**Your task**
- Import `math`
- Define radii for 4 different circular structures (in meters)
- For each, calculate and print:
  - Circumference: `2 * π * r`
  - Area: `π * r²`
  - Volume (assuming height = radius * 2): `π * r² * h`
- Round all results to 2 decimal places

**Expected output**
```
Structure 1 — radius: 0.5 m
  Circumference: 3.14 m
  Area:          0.79 m²
  Volume:        1.57 m³

Structure 2 — radius: 2.3 m
  Circumference: 14.45 m
  Area:          16.62 m²
  Volume:        76.45 m³
```

**File:** `task_04.py`

---

## Task 5 — The event countdown

**Scenario**
A concert venue's ticketing app shows fans how long until their upcoming events. The countdown display shows days, hours, and minutes until each event starts.

**Your task**
- Import `datetime`
- Define 4 upcoming event dates and times using `datetime.datetime`
- For each event:
  - Calculate the time difference from now
  - Extract total days, remaining hours, and remaining minutes from the `timedelta`
  - Format the event date as `"Saturday, April 05, 2026 at 20:00"`
- Print the countdown for each event

**Expected output**
```
Event: Rock Night Live
Date:  Saturday, April 05, 2026 at 20:00
Countdown: 6 days, 5 hours, 17 minutes

Event: Jazz Evening
Date:  Friday, April 17, 2026 at 19:30
Countdown: 18 days, 4 hours, 47 minutes
```

**File:** `task_05.py`

