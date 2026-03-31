# L26 Tasks — Abstract Classes & Interfaces

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The payment processor interface

**Scenario**
A fintech platform must support multiple payment providers. Each provider has the same interface but different internals. The abstract base class enforces the contract so any new provider just works.

**Your task**
- Create `PaymentProcessor(ABC)` with abstract methods: `charge(amount: float, description: str) -> str`, `refund(transaction_id: str, amount: float) -> str`, and abstract property `provider_name: str`
- Implement 3 concrete classes: `PaymeProcessor`, `ClickProcessor`, `VisaProcessor` — each with realistic mock logic and different fee structures
- Write `run_checkout(processor: PaymentProcessor, amount: float)` that charges and prints a receipt
- Verify that trying to instantiate `PaymentProcessor()` raises `TypeError`

**Expected output**
```
[Payme] Charged 500,000 UZS — TXN-8842 ✓
[Click] Charged 500,000 UZS — TXN-0031 ✓
[Visa]  Charged 500,000 UZS — TXN-7721 ✓

Testing abstract instantiation...
TypeError caught: Can't instantiate abstract class PaymentProcessor...
```

**File:** `task_01.py`

---

## Task 2 — The data storage backend

**Scenario**
A backend service needs to support multiple storage backends (in-memory, file, and future database). The abstract interface ensures all backends are interchangeable.

**Your task**
- Create `StorageBackend(ABC)` with abstract methods: `save(key: str, value: str) -> None`, `load(key: str) -> str | None`, `delete(key: str) -> bool`, `list_keys() -> list[str]`
- Implement `InMemoryStorage` (dict-based) and `FileStorage` (one JSON file per key, or single JSON file)
- Write a `DataService` class that takes any `StorageBackend` and has `store(key, value)`, `retrieve(key)`, `remove(key)` — delegates to the backend
- Test with both backends using identical operations

**Expected output**
```
=== InMemory Backend ===
Saved: user:001
Loaded: {"name": "Layla"}
Keys: ['user:001', 'config:app']
Deleted: True

=== File Backend ===
Saved: user:001
Loaded: {"name": "Layla"}
Keys: ['user:001', 'config:app']
```

**File:** `task_02.py`

---

## Task 3 — The report generator

**Scenario**
An analytics platform generates reports in multiple formats. Each format has the same generation pipeline but renders the output differently.

**Your task**
- Create `ReportGenerator(ABC)` with: abstract `format_header(title: str) -> str`, abstract `format_row(data: dict) -> str`, abstract `format_footer(total_rows: int) -> str`, and concrete `generate(title: str, rows: list[dict]) -> str` that calls the abstract methods in order
- Implement `PlainTextReport`, `MarkdownReport`, `HTMLReport`
- Generate the same dataset in all 3 formats and print each

**Expected output**
```
=== Plain Text ===
SALES REPORT
--------------
Ali       | 4,500,000
Sara      | 3,200,000
--------------
Total: 2 rows

=== Markdown ===
# Sales Report
| Name | Revenue |
|------|---------|
| Ali  | 4,500,000 |
...

=== HTML ===
<h1>Sales Report</h1>
<table>...
```

**File:** `task_03.py`

---

## Task 4 — The notification channel

**Scenario**
A notification system uses a `Protocol`-based interface instead of ABC, so third-party notification classes can be integrated without inheriting from a base class.

**Your task**
- Define a `NotificationChannel` Protocol with: `send(recipient: str, subject: str, body: str) -> bool`, `channel_name: str`
- Create 3 classes that satisfy the protocol WITHOUT inheriting from it: `EmailChannel`, `SMSChannel`, `WebhookChannel`
- Write `notify(channel: NotificationChannel, recipient: str, message: str) -> None`
- Demonstrate that all 3 work through the same typed interface
- Add a class `BrokenChannel` that is missing `send` — show that mypy would flag it (add a comment explaining what error would appear)

**Expected output**
```
[Email] → ali@mail.com: Order confirmed ✓
[SMS] → +998912345678: Order confirmed ✓
[Webhook] → https://hooks.example.com: Order confirmed ✓
```

**File:** `task_04.py`

---

## Task 5 — The serializer protocol

**Scenario**
A configuration management library works with multiple serialization formats. It uses a Protocol to stay decoupled from any specific implementation.

**Your task**
- Define `Serializer` Protocol: `serialize(data: dict) -> str`, `deserialize(raw: str) -> dict`, `file_extension: str`
- Implement `JsonSerializer`, `CsvSerializer` (for flat dicts), `IniSerializer` (key=value format)
- Write `ConfigManager` class that accepts any `Serializer` and has `save(filepath, data)` and `load(filepath)`
- Use all 3 serializers to save and reload the same config dict
- Verify round-trip accuracy (saved → loaded → compare)

**Expected output**
```
=== JSON Serializer ===
Saved to config.json ✓
Loaded: {'app': 'MyApp', 'debug': 'false', 'port': '8000'} ✓

=== CSV Serializer ===
Saved to config.csv ✓
Loaded: {'app': 'MyApp', 'debug': 'false', 'port': '8000'} ✓

=== INI Serializer ===
Saved to config.ini ✓
Loaded: {'app': 'MyApp', 'debug': 'false', 'port': '8000'} ✓
```

**File:** `task_05.py`

