# L15 Tasks — Decorators & Generators

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The function logger decorator

**Scenario**
A backend developer at a fintech startup needs to add logging to all sensitive functions (transfers, withdrawals, approvals) without editing each function's code. They build a reusable logging decorator.

**Your task**
- Write a `log_call` decorator that:
  - Prints `[LOG] Calling {function_name}` before the function runs
  - Prints `[LOG] {function_name} returned {result}` after
  - Uses `@functools.wraps`
- Apply it to 3 functions: `transfer_funds(amount, to)`, `approve_loan(amount)`, `get_balance(account_id)`
- Call each function and verify the logging output

**Expected output**
```
[LOG] Calling transfer_funds
[LOG] transfer_funds returned Transfer of 500,000 sum to ACC-002 complete.

[LOG] Calling approve_loan
[LOG] approve_loan returned Loan of 5,000,000 sum approved.

[LOG] Calling get_balance
[LOG] get_balance returned Balance for ACC-001: 2,300,000 sum
```

**File:** `task_01.py`

---

## Task 2 — The access control decorator

**Scenario**
An admin panel requires users to have the correct role before accessing certain functions. A decorator checks the user's role before allowing the function to execute.

**Your task**
- Write `require_role(role)` — a decorator factory that accepts a required role and returns a decorator
- The decorator checks if `current_user["role"] == role` (define `current_user` as a global dict)
- If the role matches → run the function
- If not → print `"Access denied. Required role: {role}"`
- Apply `@require_role("admin")` to `delete_user(uid)` and `@require_role("manager")` to `view_reports()`
- Test with both a matching and non-matching `current_user`

**Expected output** (current_user = {"name": "Sara", "role": "admin"})
```
Deleting user UID-042... Done.
Access denied. Required role: manager
```

**File:** `task_02.py`

---

## Task 3 — The infinite ID generator

**Scenario**
An order management system needs to generate unique sequential order IDs. Instead of storing a huge list of IDs, a generator produces them one at a time, on demand.

**Your task**
- Write `order_id_generator(prefix, start=1)` — an infinite generator that yields IDs like `"ORD-0001"`, `"ORD-0002"`, etc.
- Use `zfill(4)` or f-string formatting to zero-pad the number
- Create the generator and generate 5 IDs for a test batch of orders
- Then create a second generator with prefix `"INV-"` for invoices and generate 3 IDs

**Expected output**
```
Order IDs:
  ORD-0001
  ORD-0002
  ORD-0003
  ORD-0004
  ORD-0005

Invoice IDs:
  INV-0001
  INV-0002
  INV-0003
```

**File:** `task_03.py`

---

## Task 4 — The lazy data reader

**Scenario**
A data analyst processes a large CSV-like dataset of sales records. Instead of loading everything into memory, they write a generator that reads and yields one parsed record at a time.

**Your task**
- Create a file `sales_data.txt` with at least 8 lines in the format: `date,product,amount`
  ```
  2026-01-05,Laptop,8500000
  2026-01-06,Mouse,120000
  ...
  ```
- Write `read_sales(filename)` — a generator that opens the file and yields each line as a dictionary `{"date": ..., "product": ..., "amount": int(...)}`
- Use the generator to:
  - Print all records
  - Calculate the total sales amount
  - Filter and print only records where amount > 500,000 (use generator expression)

**Expected output**
```
All records:
  2026-01-05 | Laptop     | 8,500,000 sum
  2026-01-06 | Mouse      |   120,000 sum
  ...

Total sales: 18,470,000 sum

High-value sales (> 500,000):
  Laptop — 8,500,000 sum
  ...
```

**File:** `task_04.py`

---

## Task 5 — The retry decorator

**Scenario**
A network client for an API service sometimes fails due to temporary connection issues. A retry decorator automatically retries a function call up to N times before giving up.

**Your task**
- Write `retry(max_attempts=3, delay=0)` — a decorator factory
- The decorator calls the function and catches any `Exception`
- If it fails, waits `delay` seconds (use `time.sleep`) and tries again
- If it fails all `max_attempts` times, raises the last exception
- Print `"Attempt {n}/{max} failed: {error}"` on each failure
- Simulate a flaky function using a counter and `raise ValueError` for the first 2 calls

**Expected output**
```
Attempt 1/3 failed: Temporary connection error
Attempt 2/3 failed: Temporary connection error
[API] Data fetched successfully on attempt 3.
Result: {"status": "ok"}
```

**File:** `task_05.py`

