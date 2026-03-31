# L27 — SOLID & DRY Principles

## Why this matters
These principles are the difference between code that can be maintained, extended, and tested — and code that becomes a pile of spaghetti after six months. Every senior developer interview asks about SOLID. Every code review at a professional company applies these principles.

---

## Topics

## Single Responsibility Principle (SRP)
**A class should have only one reason to change.** Each class does one thing and does it well.

```python
# BAD — one class doing too many things
class UserManager:
    def create_user(self, name, email): ...
    def send_welcome_email(self, user): ...    # email logic mixed in
    def save_to_database(self, user): ...      # DB logic mixed in
    def generate_report(self): ...             # reporting mixed in

# GOOD — split by responsibility
class UserRepository:
    """Handles only data persistence."""
    def save(self, user: dict) -> None: ...
    def find_by_email(self, email: str) -> dict | None: ...

class EmailService:
    """Handles only email sending."""
    def send_welcome(self, user: dict) -> None: ...

class UserReporter:
    """Handles only reporting."""
    def generate_summary(self, users: list) -> str: ...

class UserService:
    """Orchestrates the above — still single responsibility: user operations."""
    def __init__(self, repo: UserRepository, email: EmailService) -> None:
        self._repo = repo
        self._email = email

    def register(self, name: str, email: str) -> dict:
        user = {"name": name, "email": email}
        self._repo.save(user)
        self._email.send_welcome(user)
        return user
```

---

## Open/Closed Principle (OCP)
**Open for extension, closed for modification.** Add new behavior without changing existing code.

```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: ...

class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price

class PercentDiscount(DiscountStrategy):
    def __init__(self, percent: float) -> None:
        self.percent = percent
    def apply(self, price: float) -> float:
        return price * (1 - self.percent / 100)

class SeasonalDiscount(DiscountStrategy):          # NEW behavior — no old code changed
    def apply(self, price: float) -> float:
        return price * 0.7

class Order:
    def __init__(self, price: float, discount: DiscountStrategy) -> None:
        self.price = price
        self.discount = discount

    def total(self) -> float:
        return self.discount.apply(self.price)     # works with ANY strategy
```

---

## Liskov Substitution Principle (LSP)
**Subclasses must be substitutable for their parent class.** If S is a subclass of T, objects of type T can be replaced by S without breaking the program.

```python
# BAD — Square breaks Rectangle's contract
class Rectangle:
    def __init__(self, w: float, h: float) -> None:
        self.width = w
        self.height = h
    def area(self) -> float:
        return self.width * self.height

class Square(Rectangle):                    # Violates LSP
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
    # Setting width alone breaks the square's constraint

# GOOD — share a common abstraction instead
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Rectangle(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.width, self.height = w, h
    def area(self) -> float:
        return self.width * self.height

class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side
    def area(self) -> float:
        return self.side ** 2
```

---

## Interface Segregation Principle (ISP)
**Clients should not be forced to depend on interfaces they do not use.** Split large interfaces into smaller, focused ones.

```python
# BAD — one fat interface
class Worker(ABC):
    @abstractmethod
    def work(self): ...
    @abstractmethod
    def eat(self): ...       # robots don't eat!
    @abstractmethod
    def sleep(self): ...     # robots don't sleep!

# GOOD — segregated interfaces
class Workable(ABC):
    @abstractmethod
    def work(self) -> None: ...

class Eatable(ABC):
    @abstractmethod
    def eat(self) -> None: ...

class HumanWorker(Workable, Eatable):     # humans need both
    def work(self) -> None: print("Human working")
    def eat(self) -> None: print("Human eating")

class RobotWorker(Workable):              # robots only need work
    def work(self) -> None: print("Robot working")
```

---

## Dependency Inversion Principle (DIP)
**Depend on abstractions, not on concretions.** High-level modules should not depend on low-level modules — both should depend on abstractions.

```python
from abc import ABC, abstractmethod

class Logger(ABC):                        # abstraction
    @abstractmethod
    def log(self, message: str) -> None: ...

class FileLogger(Logger):                 # low-level detail
    def log(self, message: str) -> None:
        with open("app.log", "a") as f:
            f.write(message + "\n")

class ConsoleLogger(Logger):              # another low-level detail
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")

class OrderService:                       # high-level module
    def __init__(self, logger: Logger) -> None:  # depends on abstraction
        self._logger = logger

    def place_order(self, order_id: str) -> None:
        self._logger.log(f"Order placed: {order_id}")  # works with ANY logger

svc = OrderService(ConsoleLogger())       # inject any implementation
svc.place_order("ORD-001")               # [LOG] Order placed: ORD-001
```

---

## DRY — Don't Repeat Yourself
**Every piece of knowledge must have a single, unambiguous representation.** Duplicated code is duplicated bugs.

```python
# BAD — same calculation duplicated
def calculate_order_tax(amount):
    return amount * 0.12

def calculate_invoice_tax(amount):
    return amount * 0.12    # same logic — if tax changes, must update 2 places

# GOOD — single source of truth
TAX_RATE = 0.12

def calculate_tax(amount: float) -> float:
    return amount * TAX_RATE

# Now used everywhere — change once, works everywhere
```

---

## Quick reference

| Principle | Core idea | Violation sign |
|---|---|---|
| SRP | One class, one responsibility | Class has unrelated methods |
| OCP | Extend via new code, not by editing | Adding features requires modifying existing classes |
| LSP | Subclasses are safe substitutes | Subclass breaks parent's behavior |
| ISP | Small, focused interfaces | Classes implement methods they don't use |
| DIP | Depend on abstractions | Class directly instantiates its dependencies |
| DRY | No duplicate logic | Same calculation/rule in 2+ places |

---

## Task list

1. The SRP refactor
2. The OCP discount engine
3. The DIP notification service
4. The DRY tax system

## LeetCode

- [Design Underground System](https://leetcode.com/problems/design-underground-system/) — 🟡 Medium — Applying SRP: separate the responsibility of recording check-ins, recording check-outs, and calculating averages.
- [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) — 🟡 Medium — Clean interface design: each method has a single clear responsibility with no overlap — ISP and SRP in practice.

