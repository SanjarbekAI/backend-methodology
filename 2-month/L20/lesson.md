# L20 — Type Hints & Dataclasses

## Why this matters
Type hints make your code self-documenting — every function signature tells the reader exactly what goes in and what comes out. Dataclasses eliminate boilerplate for data-holding objects. Together, they are standard practice in every modern Python codebase and essential for working with tools like FastAPI, Pydantic, and mypy.

---

## Topics

## Type annotations — Documenting your code's contract
Type hints are annotations that tell Python (and developers) what type each variable, parameter, and return value should be. Python does **not** enforce them at runtime — they are for documentation and tooling.

```python
# Variable annotations
name: str = "Layla"
age: int = 25
price: float = 9.99
is_active: bool = True

# Function annotations
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()

result: str = greet("Ali", 2)
print(result)    # Hello, Ali! Hello, Ali!

# Without type hints — also works, but less readable
def greet_old(name, times=1):
    return (f"Hello, {name}! " * times).strip()
```

> ⚠️ **Common mistake:** Thinking Python will crash if you pass the wrong type. It won't — type hints are advisory, not enforced. Use `mypy` (a separate tool) if you want runtime enforcement.

---

## `typing` module — Complex type hints
For lists, dicts, optional values, and more, use the `typing` module (Python 3.9+ supports built-in generic types directly).

```python
from typing import Optional, Union

# Optional — value can be the type OR None
def find_user(user_id: int) -> Optional[dict]:
    users = {1: {"name": "Ali"}, 2: {"name": "Sara"}}
    return users.get(user_id)   # returns dict or None

# Union — value can be one of several types
def process_id(id: Union[int, str]) -> str:
    return str(id).zfill(6)

# Python 3.10+ shorthand for Union
def process_id_new(id: int | str) -> str:
    return str(id).zfill(6)
```

**Python 3.9+ built-in generics (no import needed):**
```python
# Use built-in types directly for generic hints
def get_scores(names: list[str]) -> dict[str, int]:
    return {name: 0 for name in names}

def filter_active(users: list[dict]) -> list[dict]:
    return [u for u in users if u.get("active")]
```

> ⚠️ **Common mistake:** Using `List[str]` from `typing` in Python 3.9+. The modern way is `list[str]` (lowercase). Both work, but `list[str]` is cleaner.

---

## `@dataclass` — Clean data containers
A **dataclass** is a class that automatically generates `__init__`, `__repr__`, and `__eq__` for you based on the fields you declare. Perfect for data objects.

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    stock: int
    is_available: bool = True    # default value

# The @dataclass decorator auto-generates __init__, __repr__, __eq__
p1 = Product("Laptop", 8500000, 42)
p2 = Product("Mouse", 120000, 0, is_available=False)

print(p1)            # Product(name='Laptop', price=8500000, stock=42, is_available=True)
print(p1.name)       # Laptop
print(p1 == Product("Laptop", 8500000, 42))  # True — __eq__ compares field by field
```

**Without `@dataclass`, the equivalent code is:**
```python
class Product:
    def __init__(self, name, price, stock, is_available=True):
        self.name = name
        self.price = price
        self.stock = stock
        self.is_available = is_available
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, ...)"
    def __eq__(self, other):
        return (self.name == other.name and self.price == other.price ...)
```

---

## `field()` — Advanced field configuration
```python
from dataclasses import dataclass, field

@dataclass
class Order:
    customer: str
    items: list[str] = field(default_factory=list)    # mutable default — must use field()
    total: float = 0.0
    status: str = field(default="pending", repr=False) # excluded from repr

    def add_item(self, item: str, price: float) -> None:
        self.items.append(item)
        self.total += price

order = Order("Rustam")
order.add_item("Laptop", 8500000)
order.add_item("Mouse", 120000)
print(order)
# Order(customer='Rustam', items=['Laptop', 'Mouse'], total=8620000.0)
```

> ⚠️ **Common mistake:** Using a mutable default like `items: list = []`. Python will raise a `ValueError` telling you to use `field(default_factory=list)`. This is the same mutable default trap from L13 — dataclasses enforce the correct solution.

---

## `__post_init__` — Validation after initialization
```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: float
    department: str

    def __post_init__(self):                      # called automatically after __init__
        if self.salary < 0:
            raise ValueError(f"Salary cannot be negative: {self.salary}")
        self.name = self.name.strip().title()     # clean the name on creation

emp = Employee("  rustam nazarov  ", 5000000, "Engineering")
print(emp.name)     # Rustam Nazarov — cleaned automatically
```

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `x: int = 5` | Variable type annotation | `count: int = 0` |
| `def f(x: str) -> int:` | Function type hints | `def len_str(s: str) -> int:` |
| `Optional[T]` | T or None | `Optional[str]` |
| `Union[T1, T2]` | T1 or T2 | `Union[int, str]` |
| `T1 \| T2` | T1 or T2 (Python 3.10+) | `int \| str` |
| `list[T]` | List of T (3.9+) | `list[str]` |
| `dict[K, V]` | Dict with key K, value V | `dict[str, int]` |
| `@dataclass` | Auto-generate init/repr/eq | On a class definition |
| `field(default_factory=list)` | Mutable default field | `items: list = field(...)` |
| `__post_init__` | Validation after init | `def __post_init__(self):` |

---

## Task list

1. The typed user registry
2. The product catalog dataclass
3. The order system
4. The employee payroll
5. The validated config dataclass

