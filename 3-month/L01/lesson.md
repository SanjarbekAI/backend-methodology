# L23 — OOP: Classes & Objects

## Why this matters
Functions organize *actions*. Classes organize *both data and actions together*. Every major Python framework — Django, FastAPI, SQLAlchemy — is built on classes. Understanding OOP is the transition from writing scripts to designing systems.

---

## Topics

## Class definition — The blueprint
A **class** is a blueprint for creating objects. An **object** (instance) is one concrete copy built from that blueprint.

```python
class BankAccount:
    # Class body — defines the structure of every BankAccount object
    pass

# Create instances
account1 = BankAccount()   # one object
account2 = BankAccount()   # another, independent object
```

---

## `__init__` and `self` — Initializing instances
`__init__` is the **constructor** — Python calls it automatically when you create a new instance. `self` refers to the specific instance being created or used.

```python
class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner                      # instance variable
        self.balance = initial_balance          # instance variable
        self.transaction_count = 0              # instance variable with default

acc = BankAccount("Layla", 1000000)
print(acc.owner)    # Layla
print(acc.balance)  # 1000000.0
```

> ⚠️ **Common mistake:** Forgetting `self` as the first parameter of every method. `def deposit(amount)` will fail because Python passes the instance as the first argument automatically. It must be `def deposit(self, amount)`.

---

## Instance variables vs class variables
- **Instance variables** belong to one specific object (`self.x`)
- **Class variables** are shared by ALL instances of the class

```python
class Employee:
    company = "TechCorp"        # class variable — shared by all employees
    headcount = 0               # class variable — tracks total employees

    def __init__(self, name: str, salary: float) -> None:
        self.name = name        # instance variable — unique per employee
        self.salary = salary    # instance variable
        Employee.headcount += 1 # increment the shared counter

e1 = Employee("Rustam", 7500000)
e2 = Employee("Sara", 6200000)

print(e1.company)           # TechCorp
print(e2.company)           # TechCorp — same value, shared
print(Employee.headcount)   # 2

e1.company = "NewCorp"      # creates instance variable that shadows the class variable
print(e1.company)           # NewCorp — only e1's view changed
print(e2.company)           # TechCorp — e2 still sees the class variable
```

> ⚠️ **Common mistake:** Modifying mutable class variables (like lists or dicts) via `self`. This modifies the shared object for all instances. Mutable class-level defaults should almost always be instance variables initialized in `__init__`.

---

## Instance methods — Behaviors of an object
Methods are functions defined inside a class that operate on the instance (`self`).

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance
        self._history: list[str] = []    # private by convention (underscore)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._history.append(f"+{amount:,.0f}")

    def withdraw(self, amount: float) -> bool:
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        self._history.append(f"-{amount:,.0f}")
        return True

    def get_balance(self) -> float:
        return self.balance

    def print_statement(self) -> None:
        print(f"Account: {self.owner}")
        print(f"Balance: {self.balance:,.0f} sum")
        print(f"History: {', '.join(self._history)}")

acc = BankAccount("Rustam", 500000)
acc.deposit(200000)
acc.withdraw(100000)
acc.print_statement()
# Account: Rustam
# Balance: 600,000 sum
# History: +200,000, -100,000
```

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `class Name:` | Define a class | `class Car:` |
| `def __init__(self, ...):` | Constructor | `def __init__(self, name):` |
| `self.x = value` | Instance variable | `self.speed = 0` |
| `ClassName.x = value` | Class variable | `Car.total = 0` |
| `def method(self, ...):` | Instance method | `def start(self):` |
| `obj = ClassName(args)` | Create an instance | `car = Car("Toyota")` |
| `obj.attribute` | Access attribute | `car.speed` |
| `obj.method()` | Call method | `car.start()` |
| `_name` | Private by convention | `self._balance` |

---

## Task list

1. The product catalog item
2. The student record
3. The library book tracker
4. The bank account system
5. The employee roster

## LeetCode

- [Two Sum](https://leetcode.com/problems/two-sum/) — 🟢 Easy — Practice creating objects that map values to indices, just like an instance dictionary lookup.
- [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — 🟢 Easy — Model the stack as a class with push/pop methods to understand encapsulating state and behavior together.

