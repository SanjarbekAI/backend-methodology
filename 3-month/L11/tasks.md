# L33 Tasks — Practice: Full Review

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — PyStore (capstone project)

**Scenario**
You are building a complete command-line e-commerce backend as your portfolio capstone. It must demonstrate mastery of all three months of the course in one cohesive, working system.

**Your task**
- Build the full PyStore system as described in `lesson.md`
- Recommended file structure:
  ```
  pystore/
  ├── main.py              ← CLI entry point
  ├── models/
  │   ├── __init__.py
  │   ├── product.py       ← Product hierarchy
  │   ├── customer.py      ← Customer class
  │   └── order.py         ← Order dataclass
  ├── services/
  │   ├── __init__.py
  │   ├── pricing.py       ← PricingEngine hierarchy
  │   ├── order_service.py ← OrderService orchestrator
  │   └── fulfillment.py   ← Async fulfillment pipeline
  ├── repositories/
  │   ├── __init__.py
  │   └── order_repo.py    ← Repository pattern
  └── utils/
      ├── __init__.py
      ├── validators.py    ← RegEx validators
      ├── decorators.py    ← Logging decorator
      └── generators.py    ← ID generators
  ```
- Every requirement from `lesson.md` must be demonstrably present
- The system must survive invalid user input without crashing
- Data must persist between runs

**Expected flow**
```
╔══════════════════════════════╗
║        PyStore v1.0          ║
╚══════════════════════════════╝
Loaded 3 customers, 12 products, 7 orders.

1. Browse Products       5. Cancel Order
2. Add to Cart           6. Fulfill Orders (async)
3. Place Order           7. View Reports
4. View Order            8. Exit

> 6
Fulfilling 2 pending orders...
ORD-0008: payment ✓ | inventory ✓ | shipping ✓  (1.2s)
ORD-0009: payment ✓ | inventory ✓ | shipping ✓  (0.9s)
Fulfilled 2 orders in 1.24s (concurrent)

> 7
=== Sales Report ===
Total orders:    9
Fulfilled:       7
Pending:         2
Total revenue:   42,350,000 sum
Top product:     Laptop Pro (5 sold)
Cache hit rate:  68.4%

> 8
Data saved. Goodbye!
```

**File:** `main.py` (full package structure)

---

## Task 2 — The system health checker

**Scenario**
A DevOps engineer builds a standalone system health checker as a final review project. It uses a generator pipeline to collect metrics, async to check multiple services concurrently, a context manager for the reporting session, and a dataclass model for each metric.

**Your task**
- Define a `HealthMetric` dataclass with `__slots__`: `service`, `status`, `response_time`, `timestamp`
- Write `async def check_service(name, url_stub)` — simulates a health check with variable delays
- Check 6 services concurrently with `asyncio.gather()`
- Feed results through a generator pipeline: collect → validate → classify (healthy/degraded/down) → format
- Use a `ReportSession` context manager that opens a report file on enter and closes + prints summary on exit
- Apply `@lru_cache` to a `classify_service(response_time)` function called repeatedly
- Print a formatted health dashboard and save to `health_report.txt`

**Expected output**
```
=== System Health Check ===
[2026-03-30 14:25:07]

Service         Status      Response Time
api-gateway     ✅ Healthy   142ms
auth-service    ✅ Healthy   89ms
order-service   ⚠️ Degraded  1240ms
db-primary      ✅ Healthy   34ms
cache-redis     ✅ Healthy   12ms
email-worker    ❌ Down      timeout

Summary: 4 healthy | 1 degraded | 1 down
Report saved to health_report.txt
Total check time: 2.01s
```

**File:** `task_02.py`

