# L19 Tasks — RegEx & JSON

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The log parser

**Scenario**
A DevOps engineer needs to parse server log files to extract structured information: log level, timestamp, and message. The log lines have an inconsistent format and cannot be split by a simple delimiter.

**Your task**
- Define a list of 6 log lines in various formats:
  ```
  "ERROR 2026-03-30 14:25:07 Database connection failed"
  "INFO 2026-03-30 09:00:01 Server started on port 8000"
  "WARNING 2026-03-29 22:15:33 High memory usage: 87%"
  "ERROR 2026-03-30 14:26:00 Retry attempt 2 failed"
  "INFO 2026-03-30 10:30:45 User login: rustam@mail.com"
  "DEBUG 2026-03-30 11:00:00 Cache cleared"
  ```
- Use `re.match()` with groups to extract: level, date, time, message
- Print each parsed entry in a structured format
- Count and print how many ERROR entries were found

**Expected output**
```
Level: ERROR   | Date: 2026-03-30 | Time: 14:25:07 | Msg: Database connection failed
Level: INFO    | Date: 2026-03-30 | Time: 09:00:01 | Msg: Server started on port 8000
...

Total ERRORS: 2
```

**File:** `task_01.py`

---

## Task 2 — The form validator

**Scenario**
A user registration API validates form input before saving to the database. It checks email format, phone number, date of birth, and username rules using regex.

**Your task**
- Write 4 validation functions using `re`:
  - `validate_email(email)` — must match `name@domain.tld`
  - `validate_phone(phone)` — Uzbek format: `+998XXXXXXXXX` (13 chars total)
  - `validate_dob(dob)` — format `YYYY-MM-DD` only
  - `validate_username(name)` — 3–20 chars, only letters, digits, and underscores
- Test each with 2 valid and 2 invalid inputs
- Print `✓ Valid` or `✗ Invalid` for each

**Expected output**
```
Email: ali@mail.com          ✓ Valid
Email: not-an-email          ✗ Invalid
Phone: +998912345678         ✓ Valid
Phone: 012345678             ✗ Invalid
DOB: 1999-07-15              ✓ Valid
DOB: 30/03/2026              ✗ Invalid
Username: ali_dev            ✓ Valid
Username: ab                 ✗ Invalid (too short)
```

**File:** `task_02.py`

---

## Task 3 — The data cleaner

**Scenario**
A data analyst receives messy text data from a web scrape — extra whitespace, inconsistent phone formats, and HTML tags mixed in. They use regex to clean everything before analysis.

**Your task**
- Define messy strings:
  ```python
  messy_spaces = "Too   many    spaces   here"
  messy_phone = "Call us: (998) 91-234-56-78 or +998.90.876.54.32"
  messy_html = "<h1>Welcome</h1> <p>This is a <b>test</b> message.</p>"
  messy_price = "Price: $1,299.99 (was $1,499.00)"
  ```
- Use `re.sub()` to:
  - Collapse multiple spaces to one
  - Strip all non-digit characters from the phone strings
  - Remove all HTML tags from the HTML string
  - Extract both prices as floats from the price string

**Expected output**
```
Spaces cleaned: "Too many spaces here"
Phone 1: 998912345678
Phone 2: 998908765432
HTML cleaned: "Welcome This is a test message."
Prices found: [1299.99, 1499.0]
```

**File:** `task_03.py`

---

## Task 4 — The API response handler

**Scenario**
A backend service receives JSON responses from an external payment API. The service parses the response, extracts the important fields, handles errors gracefully, and logs the result.

**Your task**
- Define two JSON strings (simulate API responses):
  ```python
  success_response = '{"status": "success", "transaction_id": "TXN-8842", "amount": 250000, "currency": "UZS", "timestamp": "2026-03-30T14:25:07Z"}'
  error_response = '{"status": "error", "code": 4031, "message": "Insufficient funds", "retry": false}'
  ```
- Parse both with `json.loads()`
- If `status == "success"`: print transaction summary
- If `status == "error"`: print error details
- Then create a Python dict with 3 orders and save it to `orders.json` using `json.dump()` with indent=2
- Read it back with `json.load()` and print the loaded data

**Expected output**
```
✅ Transaction TXN-8842: 250,000 UZS at 2026-03-30T14:25:07Z

❌ Error 4031: Insufficient funds (retry: False)

Orders saved to orders.json ✓
Loaded 3 orders from file.
```

**File:** `task_04.py`

---

## Task 5 — The config file manager

**Scenario**
An application stores its runtime configuration in a JSON file. The config manager can read, update specific keys, add new settings, and save the changes back — all while preserving the structure.

**Your task**
- Create `app_config.json` programmatically with these settings:
  ```python
  {"app_name": "MyApp", "version": "1.0.0", "debug": False, "max_connections": 100, "allowed_hosts": ["localhost", "127.0.0.1"]}
  ```
- Write a function `update_config(filepath, key, value)` that:
  - Reads the JSON file
  - Updates the given key with the new value
  - Saves it back
- Call `update_config` to:
  - Set `debug` to `True`
  - Set `version` to `"1.1.0"`
  - Add a new key `"log_level"` with value `"INFO"`
- Print the final config

**Expected output**
```
Config updated: debug = True
Config updated: version = 1.1.0
Config updated: log_level = INFO

Final config:
{
  "app_name": "MyApp",
  "version": "1.1.0",
  "debug": true,
  "max_connections": 100,
  "allowed_hosts": ["localhost", "127.0.0.1"],
  "log_level": "INFO"
}
```

**File:** `task_05.py`

