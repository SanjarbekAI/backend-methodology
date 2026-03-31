# L26 — Abstract Classes & Interfaces

## Why this matters
Abstract classes define a contract: "every subclass MUST implement these methods." This turns vague design intentions into enforceable rules — essential for building plugin systems, interchangeable backends, and any architecture where multiple developers must deliver consistent implementations.

---

## Topics

## ABC module — Enforcing method contracts
The `abc` module provides `ABC` (Abstract Base Class) and `@abstractmethod`. Any class that inherits from an abstract class **must** implement all abstract methods — Python raises `TypeError` if you try to instantiate an incomplete subclass.

```python
from abc import ABC, abstractmethod

class Shape(ABC):                          # Abstract class — cannot be instantiated directly
    @abstractmethod
    def area(self) -> float:               # Must be implemented by every subclass
        pass

    @abstractmethod
    def perimeter(self) -> float:          # Must be implemented by every subclass
        pass

    def describe(self) -> str:             # Concrete method — shared by all subclasses
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

# shape = Shape()  ← TypeError: Can't instantiate abstract class Shape with abstract methods

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

circle = Circle(5)
print(circle.describe())   # Area: 78.54, Perimeter: 31.42
```

> ⚠️ **Common mistake:** Forgetting to implement one abstract method in a subclass. Python will raise a `TypeError` at instantiation time, not at definition time. Check all abstract methods are implemented.

---

## `@abstractmethod` — Required method signatures
```python
from abc import ABC, abstractmethod
from typing import Any

class DataExporter(ABC):
    """Abstract base for all export formats."""

    @abstractmethod
    def export(self, data: list[dict]) -> str:
        """Convert data to the target format string."""
        ...

    @abstractmethod
    def get_file_extension(self) -> str:
        """Return the file extension for this format."""
        ...

    def save_to_file(self, data: list[dict], filename: str) -> None:
        """Concrete shared method — uses abstract methods internally."""
        content = self.export(data)
        ext = self.get_file_extension()
        with open(f"{filename}.{ext}", "w") as f:
            f.write(content)
        print(f"Saved to {filename}.{ext}")

class CSVExporter(DataExporter):
    def export(self, data: list[dict]) -> str:
        if not data:
            return ""
        headers = ",".join(data[0].keys())
        rows = [",".join(str(v) for v in row.values()) for row in data]
        return headers + "\n" + "\n".join(rows)

    def get_file_extension(self) -> str:
        return "csv"

class JSONExporter(DataExporter):
    def export(self, data: list[dict]) -> str:
        import json
        return json.dumps(data, indent=2)

    def get_file_extension(self) -> str:
        return "json"
```

---

## Abstract properties — Required attributes
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @property
    @abstractmethod
    def fuel_type(self) -> str:       # Subclasses must expose this property
        ...

    @property
    @abstractmethod
    def max_speed(self) -> int:
        ...

class ElectricCar(Vehicle):
    @property
    def fuel_type(self) -> str:
        return "Electric"

    @property
    def max_speed(self) -> int:
        return 250
```

---

## Protocols — Structural subtyping (duck typing with types)
Python 3.8+ `Protocol` from `typing` defines an interface structurally: any class that has the required methods satisfies the protocol — **without explicitly inheriting from it**.

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:         # Any class with this method "implements" the protocol
        ...

class Circle:                      # Does NOT inherit from Drawable
    def draw(self) -> str:
        return "Drawing a circle ○"

class Square:                      # Does NOT inherit from Drawable
    def draw(self) -> str:
        return "Drawing a square □"

def render(shape: Drawable) -> None:   # Type hint accepts any Drawable
    print(shape.draw())

render(Circle())   # Drawing a circle ○
render(Square())   # Drawing a square □
```

**ABC vs Protocol:**
| | `ABC` + `@abstractmethod` | `Protocol` |
|---|---|---|
| Enforcement | At instantiation time | By type checkers (mypy) only |
| Inheritance required | Yes | No |
| Best for | Internal hierarchies | External/third-party integration |

> ⚠️ **Common mistake:** Using `ABC` when you only need type checking. `Protocol` is often lighter and more flexible for describing interfaces to external code you don't control.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `class A(ABC):` | Define abstract class | `class Shape(ABC):` |
| `@abstractmethod` | Require subclass to implement | `@abstractmethod def area(self):` |
| `@property @abstractmethod` | Required property | `@property @abstractmethod def name(self):` |
| Cannot instantiate ABC directly | Raises `TypeError` | `Shape()` → error |
| `from typing import Protocol` | Structural interface | `class Drawable(Protocol):` |
| `ABC` subclass must implement all | Or `TypeError` at instantiation | — |

---

## Task list

1. The payment processor interface
2. The data storage backend
3. The report generator
4. The notification channel
5. The serializer protocol

## LeetCode

- [Design HashMap](https://leetcode.com/problems/design-hashmap/) — 🟢 Easy — Abstract the interface first (put, get, remove) then implement — the exact workflow of ABC-driven design.
- [LRU Cache](https://leetcode.com/problems/lru-cache/) — 🟡 Medium — Design a class with a clear abstract contract (get/put), then implement the internals — an excellent exercise in interface-first thinking.

