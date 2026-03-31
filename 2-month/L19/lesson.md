# L19 — RegEx & JSON

## Why this matters
RegEx lets you search, validate, and extract patterns from text — the backbone of form validation, log parsing, and data cleaning. JSON is the universal language of APIs and configuration files. Together, these two tools are used in virtually every backend system you will ever build.

---

## Topics

## `re` module — Pattern matching with regular expressions
A **regular expression** is a pattern that describes a set of strings. Python's `re` module applies these patterns to text.

```python
import re

text = "Contact us at support@techcorp.com or sales@company.org"

# re.search() — find the FIRST match anywhere in the string
match = re.search(r"\w+@\w+\.\w+", text)
if match:
    print(match.group())    # support@techcorp.com

# re.findall() — find ALL matches, returns a list
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)               # ['support@techcorp.com', 'sales@company.org']

# re.match() — match only at the BEGINNING of the string
result = re.match(r"Contact", text)
print(bool(result))         # True — text starts with "Contact"
```

---

## Common regex patterns
```python
import re

phone = "+998-91-234-5678"
date_str = "Order placed: 2026-03-30"
log = "ERROR 2026-03-30 14:25:07 Database connection failed"

# \d — digit,  \w — word char,  \s — whitespace,  . — any char
# + — one or more,  * — zero or more,  ? — zero or one
# ^ — start of string,  $ — end of string
# [abc] — any of these chars,  [^abc] — none of these

# Extract phone number digits
digits = re.findall(r"\d+", phone)
print(digits)       # ['998', '91', '234', '5678']

# Extract a date
date_match = re.search(r"\d{4}-\d{2}-\d{2}", date_str)
print(date_match.group())   # 2026-03-30

# Validate an email
def is_valid_email(email):
    pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

print(is_valid_email("ali@mail.com"))    # True
print(is_valid_email("not-an-email"))   # False
```

---

## Groups — Capturing parts of a match
```python
import re

log_line = "ERROR 2026-03-30 14:25:07 Database connection failed"

# Parentheses () create capture groups
pattern = r"(\w+) (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (.+)"
match = re.match(pattern, log_line)

if match:
    level = match.group(1)    # ERROR
    date  = match.group(2)    # 2026-03-30
    time  = match.group(3)    # 14:25:07
    msg   = match.group(4)    # Database connection failed
    print(f"Level: {level} | Date: {date} | Time: {time}")
    print(f"Message: {msg}")
```

---

## Flags — Modifying match behaviour
```python
import re

# re.IGNORECASE (re.I) — case-insensitive matching
result = re.findall(r"python", "I love Python and PYTHON", re.IGNORECASE)
print(result)       # ['Python', 'PYTHON']

# re.sub() — substitute / replace
clean = re.sub(r"\s+", " ", "too   many    spaces")
print(clean)        # "too many spaces"

phone_clean = re.sub(r"[^\d]", "", "+998-91-234-5678")
print(phone_clean)  # "998912345678"
```

> ⚠️ **Common mistake:** Forgetting the `r""` raw string prefix. Without it, `\d` becomes an escape sequence. Always write regex patterns as `r"\d+"` not `"\d+"`.

---

## `json.dumps()` and `json.loads()` — Converting between Python and JSON
**JSON** (JavaScript Object Notation) is the standard format for data exchange between systems.

```python
import json

# Python dict → JSON string (serialization)
user = {
    "name": "Layla Karimova",
    "age": 25,
    "active": True,
    "scores": [88, 92, 78],
    "address": None
}

json_string = json.dumps(user)
print(json_string)
# {"name": "Layla Karimova", "age": 25, "active": true, "scores": [88, 92, 78], "address": null}

# Pretty-printed JSON
pretty = json.dumps(user, indent=2, ensure_ascii=False)
print(pretty)

# JSON string → Python dict (deserialization)
data = json.loads(json_string)
print(data["name"])        # Layla Karimova
print(type(data))          # <class 'dict'>
```

---

## Reading and writing JSON files
```python
import json

# Write to a JSON file
products = [
    {"id": 1, "name": "Laptop", "price": 8500000},
    {"id": 2, "name": "Mouse", "price": 120000},
]

with open("products.json", "w") as f:
    json.dump(products, f, indent=2)    # json.dump writes directly to file

# Read from a JSON file
with open("products.json", "r") as f:
    loaded = json.load(f)               # json.load reads directly from file

for product in loaded:
    print(f"{product['name']}: {product['price']:,} sum")
```

> ⚠️ **Common mistake:** Confusing `json.dumps()` (to string) with `json.dump()` (to file), and `json.loads()` (from string) with `json.load()` (from file). The `s` stands for "string."

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `re.search(pat, s)` | Find first match anywhere | `re.search(r"\d+", "abc123")` |
| `re.match(pat, s)` | Match at string start only | `re.match(r"\w+", text)` |
| `re.findall(pat, s)` | Find all matches as list | `re.findall(r"\d+", text)` |
| `re.sub(pat, repl, s)` | Replace all matches | `re.sub(r"\s+", " ", text)` |
| `match.group()` | Get matched text | `match.group(1)` |
| `r"\d+"` | One or more digits | — |
| `r"\w+"` | One or more word chars | — |
| `r"^...$"` | Full string match | `r"^\d{4}$"` |
| `json.dumps(obj)` | Python → JSON string | `json.dumps({"a": 1})` |
| `json.loads(s)` | JSON string → Python | `json.loads('{"a": 1}')` |
| `json.dump(obj, f)` | Python → JSON file | `json.dump(data, f)` |
| `json.load(f)` | JSON file → Python | `json.load(f)` |

---

## Task list

1. The log parser
2. The form validator
3. The data cleaner
4. The API response handler
5. The config file manager

