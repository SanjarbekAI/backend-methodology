# L25 Tasks — OOP: Encapsulation & Magic Methods

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The validated user profile

**Scenario**
A social platform's user model must enforce validation rules on every attribute: age must be 13–120, email must contain `@`, username must be 3–30 characters. All attributes use `@property` with setters.

**Your task**
- Create a `UserProfile` class with private attributes: `__username`, `__email`, `__age`
- Expose each via `@property` with a validated `@setter`
- Add `__str__` and `__repr__`
- Add `__eq__` (users are equal if their emails match)
- Test valid values, print the profile, and test that invalid values raise `ValueError`

**Expected output**
```
UserProfile(username='ali_dev', email='ali@mail.com', age=25)
Ali Dev — ali@mail.com (age 25)
ali_dev == ali_dev: True

Testing invalid age...
ValueError: Age must be between 13 and 120. Got: 200
```

**File:** `task_01.py`

---

## Task 2 — The temperature converter class

**Scenario**
A scientific instrument library models temperature readings as objects. The class stores internally in Celsius and exposes Fahrenheit and Kelvin as computed read-only properties.

**Your task**
- Create `Temperature` with private `__celsius`
- `@property celsius` with setter (validates ≥ −273.15)
- `@property fahrenheit` — read-only computed: `C * 9/5 + 32`
- `@property kelvin` — read-only computed: `C + 273.15`
- `__str__`: `"25.0°C / 77.0°F / 298.2K"`
- `__repr__`: `"Temperature(celsius=25.0)"`
- `__eq__`, `__lt__`, `__gt__` for comparisons
- Create 4 temperature objects and sort them using `sorted()`

**Expected output**
```
25.0°C / 77.0°F / 298.15K
Temperature(celsius=25.0)
Sorted (cold to hot): [-10.0°C, 0.0°C, 25.0°C, 100.0°C]
```

**File:** `task_02.py`

---

## Task 3 — The inventory container

**Scenario**
A warehouse system models an inventory bin as a container object. It supports Python's container protocols: `len()`, `in`, indexing, and iteration.

**Your task**
- Create `InventoryBin` with `bin_id`, `capacity`, private `__items: list`
- `add(item: str) -> bool` — adds item if below capacity
- `remove(item: str) -> bool`
- `__len__` — number of items
- `__contains__` — `"Laptop" in bin`
- `__getitem__` — `bin[0]` returns item at index
- `__iter__` — allows `for item in bin:`
- `__str__` — `"BIN-A1 (3/10 items)"`
- Create 2 bins, fill them, iterate over one, check membership in the other

**Expected output**
```
BIN-A1 (3/10 items)
Items in BIN-A1:
  - Laptop
  - Mouse
  - Keyboard
"Monitor" in BIN-A2: True
len(BIN-A2): 2
```

**File:** `task_03.py`

---

## Task 4 — The money type

**Scenario**
A fintech application needs a `Money` class that behaves like a numeric type — supporting addition, subtraction, comparison, and display — while enforcing currency matching and non-negative amounts.

**Your task**
- Create `Money` with `amount: float` and `currency: str`
- `__add__`: adds two Money objects if same currency, else raises `ValueError`
- `__sub__`: subtracts, result must be ≥ 0 else raises `ValueError`
- `__mul__`: `Money * float` (e.g., for tax or discount)
- `__eq__`, `__lt__`, `__gt__`
- `__str__`: `"500,000 UZS"`
- `__repr__`: `"Money(amount=500000, currency='UZS')"`
- Demonstrate all operations with realistic financial calculations

**Expected output**
```
500,000 UZS + 200,000 UZS = 700,000 UZS
700,000 UZS - 150,000 UZS = 550,000 UZS
500,000 UZS × 1.12 = 560,000.0 UZS
500,000 UZS == 500,000 UZS: True
500,000 UZS > 200,000 UZS: True
```

**File:** `task_04.py`

---

## Task 5 — The playlist manager

**Scenario**
A music app models playlists as objects supporting Python's built-in protocols. Playlists can be combined, compared by length, and iterated over naturally.

**Your task**
- Create `Playlist` with `name: str`, private `__tracks: list[str]`
- `add_track(title)`, `remove_track(title)`
- `__len__` — track count
- `__contains__` — `"Song" in playlist`
- `__add__` — merges two playlists into a new one (combined name + combined tracks, deduped)
- `__eq__` — equal if same tracks (order ignored: compare as sets)
- `__str__` — `"Chill Vibes (12 tracks)"`
- `__repr__`
- Create 3 playlists, merge two, check membership, print all

**Expected output**
```
Chill Vibes (5 tracks)
Workout Mix (4 tracks)
Merged: Chill Vibes + Workout Mix (8 tracks)
"Levitating" in Merged: True
Chill Vibes == Workout Mix: False
```

**File:** `task_05.py`

