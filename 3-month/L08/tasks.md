# L30 Tasks — Context Managers & Metaclasses

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The resource manager

**Scenario**
A data processing pipeline opens, processes, and closes multiple resources. A context manager ensures resources are always released even if an error occurs mid-processing.

**Your task**
- Create a `ManagedResource` class with `__enter__` and `__exit__`
- It takes a `name: str` and simulates acquiring/releasing a resource (print messages)
- In `__exit__`, if an exception occurred, log the error and return `False`
- Use it to manage 3 resources in nested `with` blocks
- Demonstrate that even when an exception is raised inside a `with` block, `__exit__` always runs

**Expected output**
```
Acquiring: database_connection
Acquiring: file_handle
Acquiring: cache_client
Processing...
Releasing: cache_client
Releasing: file_handle
Releasing: database_connection
All resources released cleanly.

--- Error test ---
Acquiring: api_connection
Error in __exit__: ValueError - something broke
Releasing: api_connection
```

**File:** `task_01.py`

---

## Task 2 — The retry context manager

**Scenario**
A network client sometimes fails due to transient errors. A context manager wraps the operation and automatically retries up to N times before giving up.

**Your task**
- Use `@contextmanager` from `contextlib` to write `retry(max_attempts: int, delay: float = 0)`
- Inside the generator: attempt the `yield` in a loop, catch exceptions, retry with delay
- If all attempts fail, re-raise the last exception
- Print attempt number and error message on each failure
- Test with a function that fails 2 times then succeeds on the 3rd attempt

**Expected output**
```
Attempt 1/3 failed: Connection refused
Attempt 2/3 failed: Connection refused
Attempt 3/3 succeeded.
Result: {"status": "ok"}
```

**File:** `task_02.py`

---

## Task 3 — The singleton database pool

**Scenario**
A backend service must have exactly one database connection pool, no matter how many modules try to create one. A metaclass enforces the singleton pattern.

**Your task**
- Write `SingletonMeta(type)` metaclass
- Apply it to `ConnectionPool` class: `host: str`, `port: int`, `max_connections: int`
- `ConnectionPool` has methods: `get_connection() -> str`, `release_connection(conn: str) -> None`, `status() -> str`
- Demonstrate that creating `ConnectionPool("localhost", 5432, 10)` multiple times always returns the same instance
- Show `pool1 is pool2` is `True`

**Expected output**
```
Pool created: localhost:5432 (max 10)
Pool created: remotehost:5432 (max 20)  ← this call is ignored

pool1 is pool2: True
pool1.host: localhost  ← first creation wins
Pool status: 0/10 connections in use
```

**File:** `task_03.py`

---

## Task 4 — The auto-validating metaclass

**Scenario**
A data modeling library wants every class that defines `REQUIRED_FIELDS` to automatically validate that all required fields are present when an instance is created. The metaclass injects this validation.

**Your task**
- Write `ValidatingMeta(type)` that:
  - In `__new__`, checks if the class defines `REQUIRED_FIELDS`
  - Wraps `__init__` to validate that all `REQUIRED_FIELDS` are passed as kwargs or set as attributes
  - Raises `ValueError` if any required field is missing after `__init__`
- Apply it to `UserModel` and `OrderModel` with different required fields
- Test with valid and invalid data

**Expected output**
```
UserModel created: Rustam (ali@mail.com)
OrderModel created: ORD-001

Testing missing fields...
ValueError: UserModel missing required field: 'email'
ValueError: OrderModel missing required field: 'customer_id'
```

**File:** `task_04.py`

---

## Task 5 — The plugin registry

**Scenario**
A document processing system allows developers to register custom processor plugins. A metaclass automatically registers every subclass in a central registry, enabling plugin discovery without manual registration.

**Your task**
- Write `PluginMeta(type)` that maintains a `registry: dict[str, type]` class variable
- Every subclass of `BaseProcessor` is auto-registered under its class name
- `BaseProcessor` itself must NOT appear in the registry
- Implement 3 processors: `PDFProcessor`, `WordProcessor`, `ImageProcessor` — each has `process(filepath: str) -> str`
- Write `get_processor(file_extension: str) -> BaseProcessor | None` that looks up the right processor from the registry
- Demonstrate auto-registration and lookup

**Expected output**
```
Registered plugins: ['PDFProcessor', 'WordProcessor', 'ImageProcessor']

Processing report.pdf...
[PDF] Processing report.pdf: extracted 42 pages

Processing letter.docx...
[Word] Processing letter.docx: extracted 3 pages

Unknown: .xlsx → No processor registered for this format.
```

**File:** `task_05.py`

