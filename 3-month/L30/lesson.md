# L30 — Context Managers & Metaclasses

## Why this matters
Context managers are how Python guarantees cleanup — they power `with open()`, database transactions, and lock acquisition. Metaclasses control how classes themselves are created — they are used in Django's ORM, SQLAlchemy, and every major Python framework you will work with.

---

## Topics

## `__enter__` and `__exit__` — Custom context managers
Any class with `__enter__` and `__exit__` methods can be used with the `with` statement.

```python
import time

class Timer:
    """Context manager that measures execution time."""

    def __enter__(self) -> "Timer":
        self.start = time.perf_counter()
        return self                          # returned as the 'as' target

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.4f}s")
        return False                         # False = don't suppress exceptions

with Timer() as t:
    total = sum(x ** 2 for x in range(1_000_000))
# Elapsed: 0.0823s

# exc_type, exc_val, exc_tb are None if no exception occurred
# return True to suppress the exception, False to let it propagate
```

**Database transaction context manager:**
```python
class DatabaseTransaction:
    def __init__(self, connection) -> None:
        self.conn = connection

    def __enter__(self) -> "DatabaseTransaction":
        self.conn.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is None:
            self.conn.commit()           # success — commit
            print("Transaction committed.")
        else:
            self.conn.rollback()         # error — rollback
            print(f"Transaction rolled back: {exc_val}")
        return False                     # always let exceptions propagate
```

> ⚠️ **Common mistake:** Returning `True` from `__exit__` accidentally. This silences exceptions, which can hide bugs. Only return `True` when you intentionally want to swallow an exception.

---

## `contextlib` — Easier context managers with generators
`contextlib.contextmanager` lets you write a context manager as a generator function — cleaner for simple cases.

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield                                 # everything inside 'with' runs here
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{label}] {elapsed:.4f}s")

with timer("data processing"):
    data = [x ** 2 for x in range(500000)]

@contextmanager
def managed_file(path: str, mode: str):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()                             # guaranteed cleanup

with managed_file("output.txt", "w") as f:
    f.write("Hello from context manager!")
```

---

## `type()` — The metaclass in disguise
In Python, everything is an object — including classes. `type` is the metaclass that creates all classes.

```python
# A class definition is syntactic sugar for calling type()
class Dog:
    species = "Canis familiaris"
    def bark(self): return "Woof!"

# Equivalent to:
Dog = type(
    "Dog",                                    # class name
    (object,),                               # base classes (tuple)
    {"species": "Canis familiaris",           # class body (dict)
     "bark": lambda self: "Woof!"}
)

print(type(Dog))     # <class 'type'>
print(type(42))      # <class 'int'>
print(type("hello")) # <class 'str'>
```

---

## `__new__` and metaclass basics
A **metaclass** is a class whose instances are classes. You define one by inheriting from `type`.

```python
class SingletonMeta(type):
    """Metaclass that ensures only one instance per class exists."""
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, host: str) -> None:
        self.host = host
        print(f"Connection created: {host}")

db1 = DatabaseConnection("localhost")   # Connection created: localhost
db2 = DatabaseConnection("remotehost")  # No output! Same instance returned
print(db1 is db2)                        # True — same object!
print(db2.host)                          # localhost — first creation wins
```

**Auto-registering classes with a metaclass:**
```python
class PluginMeta(type):
    registry: dict[str, type] = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:                                  # skip the base class itself
            PluginMeta.registry[name] = cls
        return cls

class Plugin(metaclass=PluginMeta):
    pass

class JSONPlugin(Plugin): pass
class XMLPlugin(Plugin):  pass

print(PluginMeta.registry)
# {'JSONPlugin': <class 'JSONPlugin'>, 'XMLPlugin': <class 'XMLPlugin'>}
```

> ⚠️ **Common mistake:** Reaching for metaclasses when a class decorator would suffice. Metaclasses are powerful but complex. Use them only when you need to control class creation itself — most framework-level work. For adding behavior to instances, use decorators or regular inheritance.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `def __enter__(self):` | Setup on `with` entry | Return resource |
| `def __exit__(self, et, ev, tb):` | Cleanup on `with` exit | Return `False` normally |
| `@contextmanager` | Generator-based context manager | `yield` splits enter/exit |
| `type(name, bases, dict)` | Dynamically create a class | `type("Dog", (object,), {})` |
| `class Meta(type):` | Define a metaclass | `class SingletonMeta(type):` |
| `class A(metaclass=Meta):` | Use a metaclass | `class DB(metaclass=SingletonMeta):` |
| `def __new__(mcs, name, bases, ns):` | Called at class creation | Intercept/modify class |

---

## Task list

1. The resource manager
2. The retry context manager
3. The singleton database pool
4. The auto-validating metaclass
5. The plugin registry

## LeetCode

- [Design Log Storage System](https://leetcode.com/problems/design-log-storage-system/) — 🟡 Medium — A context manager fits naturally here: `with log_storage.session():` wraps the log operations the same way a transaction context manager wraps DB operations.
- [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) — 🟡 Medium — Building `TrieNode` classes that control their own creation is excellent practice before working with `__new__` and metaclass-controlled instantiation.

