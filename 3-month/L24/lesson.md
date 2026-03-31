# L24 — OOP: Inheritance & Polymorphism

## Why this matters
Inheritance lets you build specialized versions of a class without rewriting shared logic. Polymorphism lets different objects respond to the same call in their own way — the foundation of plugin systems, payment gateways, and notification services where you swap implementations at runtime.

---

## Topics

## Inheritance — Building on existing classes
A **child class** (subclass) inherits all attributes and methods from its **parent class** (superclass) and can add or override them.

```python
class Vehicle:                          # parent class
    def __init__(self, brand: str, speed: int) -> None:
        self.brand = brand
        self.speed = speed

    def describe(self) -> str:
        return f"{self.brand} — max speed: {self.speed} km/h"

    def move(self) -> str:
        return "Moving..."

class Car(Vehicle):                     # Car inherits from Vehicle
    def __init__(self, brand: str, speed: int, doors: int) -> None:
        super().__init__(brand, speed)  # call parent's __init__
        self.doors = doors              # add child-specific attribute

    def describe(self) -> str:         # override parent method
        base = super().describe()      # reuse parent's logic
        return f"{base}, {self.doors} doors"

class Motorcycle(Vehicle):
    def move(self) -> str:             # override move()
        return "Riding on 2 wheels..."

car = Car("Toyota", 180, 4)
moto = Motorcycle("Honda", 220)

print(car.describe())    # Toyota — max speed: 180 km/h, 4 doors
print(moto.move())       # Riding on 2 wheels...
print(moto.describe())   # Honda — max speed: 220 km/h  ← inherited unchanged
```

> ⚠️ **Common mistake:** Forgetting `super().__init__()` in the child's `__init__`. Without it, the parent's instance variables are never created, and any method that accesses them will crash with `AttributeError`.

---

## `super()` — Accessing the parent
`super()` gives you access to the parent class's methods. Use it to extend (not replace) parent behavior.

```python
class Animal:
    def __init__(self, name: str, sound: str) -> None:
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says: {self.sound}"

class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name, "Woof")  # parent handles name and sound
        self.breed = breed              # dog-specific

    def speak(self) -> str:
        parent_speak = super().speak()  # reuse parent's speak
        return f"{parent_speak} (breed: {self.breed})"

dog = Dog("Rex", "German Shepherd")
print(dog.speak())   # Rex says: Woof (breed: German Shepherd)
```

---

## Method overriding — Redefining inherited behavior
A child class can completely replace a parent method by defining a method with the same name.

```python
class PaymentProcessor:
    def process(self, amount: float) -> str:
        return f"Processing {amount} sum..."

    def refund(self, amount: float) -> str:
        return f"Refunding {amount} sum..."

class ClickPayProcessor(PaymentProcessor):
    def process(self, amount: float) -> str:       # override
        return f"[ClickPay] Charging {amount} sum via mobile wallet."

class CardProcessor(PaymentProcessor):
    def process(self, amount: float) -> str:       # override
        return f"[Card] Charging {amount} sum via Visa/MasterCard."

    def process_with_3ds(self, amount: float) -> str:   # new method
        return f"[Card+3DS] Secure charge: {amount} sum"
```

---

## Multiple inheritance — Inheriting from several parents
Python supports inheriting from more than one parent class. Use carefully.

```python
class Flyable:
    def fly(self) -> str:
        return "Flying..."

class Swimmable:
    def swim(self) -> str:
        return "Swimming..."

class Duck(Flyable, Swimmable):   # inherits from both
    def describe(self) -> str:
        return f"I can {self.fly()} and {self.swim()}"

duck = Duck()
print(duck.describe())   # I can Flying... and Swimming...
print(isinstance(duck, Flyable))     # True
print(isinstance(duck, Swimmable))   # True
```

> ⚠️ **Common mistake:** Overusing multiple inheritance. It creates the **diamond problem** — ambiguous method resolution. Use it for **mixins** (small, focused classes adding one capability) and prefer composition for everything else.

---

## Polymorphism — One interface, many behaviors
Polymorphism means different classes can be used interchangeably if they share the same method names. Python uses **duck typing** — if it has the method, it works.

```python
class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"[Email] Sending: {message}")

class SMSNotifier:
    def send(self, message: str) -> None:
        print(f"[SMS] Sending: {message}")

class PushNotifier:
    def send(self, message: str) -> None:
        print(f"[Push] Sending: {message}")

def notify_all(notifiers: list, message: str) -> None:
    for notifier in notifiers:
        notifier.send(message)     # same call — different behavior per type

notifiers = [EmailNotifier(), SMSNotifier(), PushNotifier()]
notify_all(notifiers, "Your order has shipped!")
# [Email] Sending: Your order has shipped!
# [SMS] Sending: Your order has shipped!
# [Push] Sending: Your order has shipped!
```

---

## Duck typing — If it walks like a duck...
Python doesn't require a shared base class for polymorphism. If an object has the method, it works.

```python
class CSVExporter:
    def export(self, data: list) -> str:
        return ",".join(str(x) for x in data)

class JSONExporter:
    def export(self, data: list) -> str:
        import json
        return json.dumps(data)

def run_export(exporter, data: list) -> None:
    print(exporter.export(data))   # works for any object with .export()

run_export(CSVExporter(), [1, 2, 3])   # 1,2,3
run_export(JSONExporter(), [1, 2, 3])  # [1, 2, 3]
```

> ⚠️ **Common mistake:** Checking types with `isinstance` everywhere instead of trusting duck typing. `if type(obj) == Dog:` is almost always the wrong approach. Design classes to share interfaces instead.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `class Child(Parent):` | Inherit from Parent | `class Dog(Animal):` |
| `super().__init__(...)` | Call parent's constructor | `super().__init__(name)` |
| `super().method()` | Call parent's method | `super().speak()` |
| Method with same name | Override parent method | `def speak(self):` in child |
| `class C(A, B):` | Multiple inheritance | `class Duck(Flyable, Swimmable):` |
| `isinstance(obj, Class)` | Check if obj is an instance | `isinstance(dog, Animal)` |
| `issubclass(Child, Parent)` | Check class hierarchy | `issubclass(Dog, Animal)` |

---

## Task list

1. The vehicle fleet
2. The payment gateway
3. The notification system
4. The shape area calculator
5. The employee hierarchy

## LeetCode

- [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) — 🟢 Easy — A classic problem that can be modeled as a class hierarchy where each "step strategy" is a subclass overriding the `count_ways` method.
- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) — 🟢 Easy — The `ListNode` class demonstrates how objects reference other objects — the foundation of inheritance and object composition.

