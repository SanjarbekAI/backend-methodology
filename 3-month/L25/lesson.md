# L25 — OOP: Encapsulation & Magic Methods

## Why this matters
Encapsulation protects your object's internal state from being broken by outside code. Magic methods let your custom classes behave like built-in Python types — you can use `len()`, `+`, `==`, and `print()` on your own objects, making them feel native to the language.

---

## Topics

## Private & protected attributes — Controlling access
Python uses naming conventions to signal how attributes should be accessed:

```python
class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner           # public — anyone can read/write
        self._bank_code = "UZB001"   # protected — intended for internal/subclass use only
        self.__balance = balance     # private — name-mangled, strongest signal

    def get_balance(self) -> float:
        return self.__balance        # controlled read access

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount     # only the class can modify __balance directly

acc = BankAccount("Layla", 1000000)
print(acc.owner)             # OK — public
print(acc._bank_code)        # Works but signals: "don't do this from outside"
# print(acc.__balance)       # AttributeError — name was mangled to _BankAccount__balance
print(acc.get_balance())     # 1000000 — correct way to access
```

**Name mangling:** `__balance` becomes `_BankAccount__balance` internally — not truly private, but strongly discourages outside access.

> ⚠️ **Common mistake:** Thinking `__` makes an attribute truly inaccessible. Python name-mangles it but doesn't lock it. `acc._BankAccount__balance` still works. The convention is about signaling intent, not security.

---

## `@property` — Controlled attribute access
`@property` turns a method into an attribute-style accessor. Add `@attr.setter` to allow controlled writes.

```python
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:       # read: temp.celsius
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:   # write: temp.celsius = 25
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:    # computed property — read-only
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0
temp.celsius = 100       # calls the setter
# temp.celsius = -300    # ValueError!
```

> ⚠️ **Common mistake:** Forgetting to name the setter the same as the property. `@celsius.setter` must match `@property def celsius`. A mismatch creates a separate unrelated attribute.

---

## `__str__` and `__repr__` — String representations
```python
class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        # Human-readable — used by print() and str()
        return f"{self.name} — {self.price:,.0f} sum"

    def __repr__(self) -> str:
        # Developer-readable — used in REPL, debugging, lists
        return f"Product(name={self.name!r}, price={self.price})"

p = Product("Laptop", 8500000)
print(p)           # Laptop — 8,500,000 sum       ← __str__
print(repr(p))     # Product(name='Laptop', price=8500000)  ← __repr__
print([p])         # [Product(name='Laptop', price=8500000)]  ← list uses __repr__
```

> ⚠️ **Common mistake:** Only defining `__str__` and not `__repr__`. Always define `__repr__` — it's used in debugging, logging, and inside collections. If only one can be defined, `__repr__` is more important.

---

## `__len__`, `__eq__`, `__add__` — Operator magic
```python
class ShoppingCart:
    def __init__(self) -> None:
        self._items: list[dict] = []

    def add(self, name: str, price: float) -> None:
        self._items.append({"name": name, "price": price})

    def __len__(self) -> int:              # len(cart)
        return len(self._items)

    def __eq__(self, other: object) -> bool:  # cart1 == cart2
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        return self._items == other._items

    def __add__(self, other: "ShoppingCart") -> "ShoppingCart":  # cart1 + cart2
        merged = ShoppingCart()
        merged._items = self._items + other._items
        return merged

    def __str__(self) -> str:
        total = sum(i["price"] for i in self._items)
        return f"Cart: {len(self)} items, total {total:,.0f} sum"

cart1 = ShoppingCart()
cart1.add("Laptop", 8500000)
cart2 = ShoppingCart()
cart2.add("Mouse", 120000)

print(len(cart1))        # 1
merged = cart1 + cart2
print(merged)            # Cart: 2 items, total 8,620,000 sum
print(cart1 == cart2)    # False
```

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `self._x` | Protected (by convention) | `self._code = "A1"` |
| `self.__x` | Private (name-mangled) | `self.__balance = 0` |
| `@property` | Read-only attribute accessor | `@property def name(self):` |
| `@name.setter` | Write accessor with validation | `@name.setter def name(self, v):` |
| `__str__` | `print(obj)` → human string | `def __str__(self) -> str:` |
| `__repr__` | `repr(obj)` → dev string | `def __repr__(self) -> str:` |
| `__len__` | `len(obj)` | `def __len__(self) -> int:` |
| `__eq__` | `obj1 == obj2` | `def __eq__(self, other):` |
| `__add__` | `obj1 + obj2` | `def __add__(self, other):` |
| `__contains__` | `x in obj` | `def __contains__(self, item):` |
| `__getitem__` | `obj[key]` | `def __getitem__(self, key):` |

---

## Task list

1. The validated user profile
2. The temperature converter class
3. The inventory container
4. The money type
5. The playlist manager

## LeetCode

- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — 🟢 Easy — The `ListNode` class uses encapsulation to protect `val` and `next`; reversing it exercises your understanding of object references and mutation.
- [Min Stack](https://leetcode.com/problems/min-stack/) — 🟢 Easy — Design a class with private state and a clean public interface — the core of encapsulation.

