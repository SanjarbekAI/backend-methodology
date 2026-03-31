# L20 Tasks — Type Hints & Dataclasses

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The typed user registry

**Scenario**
A user management system standardizes all its functions with type hints so the team can safely refactor and scale the codebase. The functions are straightforward but all must be fully annotated.

**Your task**
- Write 4 fully type-annotated functions:
  - `create_user(name: str, email: str, age: int) -> dict[str, str | int]`
  - `get_user_email(user: dict[str, str | int]) -> str`
  - `is_adult(user: dict[str, str | int]) -> bool`
  - `find_user(users: list[dict], email: str) -> dict | None`
- Create 3 users, store them in a list, and call all 4 functions
- Print results clearly

**Expected output**
```
Created: {'name': 'Layla', 'email': 'layla@mail.com', 'age': 25}
Email: layla@mail.com
Adult: True
Found: {'name': 'Layla', 'email': 'layla@mail.com', 'age': 25}
Search for unknown@mail.com: None
```

**File:** `task_01.py`

---

## Task 2 — The product catalog dataclass

**Scenario**
An e-commerce platform's inventory system models products as dataclasses. The team uses type-annotated dataclasses so IDEs and linters can catch mistakes before they reach production.

**Your task**
- Create a `Product` dataclass with: `id: int`, `name: str`, `price: float`, `category: str`, `stock: int`, `is_available: bool = True`
- Create 5 product instances
- Write a typed function `filter_products(products: list[Product], category: str) -> list[Product]` that returns products in the given category
- Write `apply_discount(product: Product, percent: float) -> Product` that returns a new product with updated price
- Print filtered results and a discounted product

**Expected output**
```
Electronics:
  Product(id=1, name='Laptop', price=8500000, ...)
  Product(id=2, name='Webcam', price=580000, ...)

Discounted: Product(id=1, name='Laptop', price=7225000.0, ...)
```

**File:** `task_02.py`

---

## Task 3 — The order system

**Scenario**
A restaurant's order management backend models orders as dataclasses. Each order accumulates items and calculates a running total. Orders have a mutable item list that must use `field(default_factory=list)`.

**Your task**
- Create an `OrderItem` dataclass: `name: str`, `price: float`, `qty: int`
- Create an `Order` dataclass: `order_id: str`, `customer: str`, `items: list[OrderItem] = field(default_factory=list)`, `status: str = "open"`
- Add a method `add_item(self, item: OrderItem) -> None`
- Add a method `total(self) -> float` that returns the sum of `item.price * item.qty`
- Add a method `close(self) -> None` that sets status to `"closed"`
- Create 2 orders, add items, print totals, close one order

**Expected output**
```
Order ORD-001 (Rustam) — open
  2x Burger @ 35,000 = 70,000
  1x Cola   @ 10,000 = 10,000
Total: 80,000 sum

Order ORD-002 (Layla) — closed
  1x Pizza  @ 45,000 = 45,000
Total: 45,000 sum
```

**File:** `task_03.py`

---

## Task 4 — The employee payroll

**Scenario**
An HR system uses a dataclass to model employees. The `__post_init__` method validates the data and automatically formats the name. A typed function calculates net salary after tax.

**Your task**
- Create an `Employee` dataclass: `name: str`, `department: str`, `gross_salary: float`, `tax_rate: float = 0.12`
- Use `__post_init__` to:
  - Strip and title-case the name
  - Raise `ValueError` if gross_salary ≤ 0
  - Raise `ValueError` if tax_rate not between 0 and 1
- Write a typed function `calculate_net(emp: Employee) -> float`
- Write a typed function `generate_payslip(emp: Employee) -> str` that returns a formatted multi-line payslip string
- Create 3 employees and print their payslips

**Expected output**
```
========== PAYSLIP ==========
Employee:   Rustam Nazarov
Department: Engineering
Gross:      7,500,000 sum
Tax (12%):    900,000 sum
Net:        6,600,000 sum
=============================
```

**File:** `task_04.py`

---

## Task 5 — The validated config dataclass

**Scenario**
A web application stores its startup configuration in a typed dataclass. The config is loaded from a JSON file and validated on load. Invalid configs must raise clear errors.

**Your task**
- Create a `AppConfig` dataclass: `app_name: str`, `version: str`, `debug: bool`, `port: int`, `allowed_hosts: list[str]`, `max_connections: int = 100`
- Use `__post_init__` to validate:
  - `port` must be between 1024 and 65535
  - `max_connections` must be > 0
  - `app_name` must not be empty
- Write `load_config(filepath: str) -> AppConfig` that reads a JSON file and returns an `AppConfig` instance
- Create the JSON file programmatically, load it, and print the config
- Test that an invalid port raises a `ValueError`

**Expected output**
```
Config loaded successfully:
AppConfig(app_name='MyApp', version='1.0.0', debug=False, port=8000, allowed_hosts=['localhost'], max_connections=100)

Testing invalid config...
ValueError: Port must be between 1024 and 65535. Got: 80
```

**File:** `task_05.py`

