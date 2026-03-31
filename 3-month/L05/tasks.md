# L27 Tasks — SOLID & DRY Principles

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The SRP refactor

**Scenario**
A developer at a startup wrote a single `OrderManager` class that handles everything: creating orders, sending confirmation emails, saving to a file, and generating reports. Your job is to refactor it following SRP.

**Your task**
- Start with this violating class (copy it into your file):
  ```python
  class OrderManager:
      def create_order(self, customer, items, total): ...
      def send_confirmation_email(self, customer, order_id): ...
      def save_order_to_file(self, order): ...
      def generate_monthly_report(self, orders): ...
      def apply_discount(self, order, percent): ...
  ```
- Identify the responsibilities and split into correctly-scoped classes
- Each class must have a docstring explaining its single responsibility
- Wire them together in an `OrderService` orchestrator
- Demonstrate the full workflow: create → discount → save → email → report

**Expected output**
```
Order ORD-0042 created for Rustam — Total: 450,000 sum
Discount applied: 10% → 405,000 sum
Order saved to orders.json ✓
Email sent to rustam@mail.com ✓
Monthly report: 1 order, 405,000 sum total
```

**File:** `task_01.py`

---

## Task 2 — The OCP discount engine

**Scenario**
An e-commerce platform's discount system keeps needing new discount types every season. Following OCP, adding a new discount type must never require modifying existing discount code.

**Your task**
- Create `DiscountStrategy(ABC)` with abstract `apply(price: float) -> float` and abstract property `description: str`
- Implement: `NoDiscount`, `PercentDiscount(percent)`, `FixedAmountDiscount(amount)`, `BuyOneGetOneDiscount` (50% off), `LoyaltyDiscount(tier)` (Bronze=5%, Silver=10%, Gold=20%)
- Write `PriceCalculator` that takes any `DiscountStrategy` and calculates final price
- Add a brand new `FlashSaleDiscount(percent, max_discount)` to prove no existing code changes

**Expected output**
```
Original:    500,000 sum
No discount: 500,000 sum
Percent 15%: 425,000 sum
Fixed 50k:   450,000 sum
BOGO:        250,000 sum
Gold Loyal:  400,000 sum
Flash Sale:  350,000 sum (capped at 150,000 discount)
```

**File:** `task_02.py`

---

## Task 3 — The DIP notification service

**Scenario**
A user authentication service sends notifications (password reset, login alert, account locked). Following DIP, it must not depend on any specific notification implementation.

**Your task**
- Define `NotificationService(ABC)` with abstract `notify(user_email: str, subject: str, body: str) -> None`
- Implement `EmailNotificationService`, `SMSNotificationService`, `MockNotificationService` (for testing — just records calls)
- Create `AuthService` that accepts `NotificationService` in its constructor (dependency injection) and has: `reset_password(email)`, `alert_new_login(email, ip)`, `lock_account(email)`
- Run the same `AuthService` operations with all 3 notification backends
- Show that swapping backends requires zero changes to `AuthService`

**Expected output**
```
=== Email Backend ===
[Email] → ali@mail.com: "Password Reset" sent ✓
[Email] → ali@mail.com: "New Login from 192.168.1.1" sent ✓

=== Mock Backend (tests) ===
MockNotifier recorded 2 calls.
Call 1: ali@mail.com — Password Reset
Call 2: ali@mail.com — New Login from 192.168.1.1
```

**File:** `task_03.py`

---

## Task 4 — The DRY tax system

**Scenario**
A billing system calculates taxes for different document types: invoices, receipts, and payroll. Currently the tax rate is hardcoded in three different places. Your task is to eliminate the duplication and create a single source of truth.

**Your task**
- Start with this violating code (copy it and refactor):
  ```python
  def calculate_invoice_total(subtotal):
      tax = subtotal * 0.12
      return subtotal + tax

  def calculate_receipt_total(subtotal):
      tax = subtotal * 0.12   # duplicated!
      return subtotal + tax

  def calculate_payroll_deduction(gross):
      deduction = gross * 0.12  # duplicated again!
      return gross - deduction
  ```
- Create a `TaxConfig` class or module constant as the single source of truth
- Refactor all three functions to use it
- Add a `TaxCalculator` class with methods for each document type
- Demonstrate: change the tax rate in one place and all calculations update

**Expected output**
```
Current tax rate: 12%

Invoice: 1,000,000 + 120,000 tax = 1,120,000 sum
Receipt: 500,000 + 60,000 tax = 560,000 sum
Payroll: 3,000,000 - 360,000 tax = 2,640,000 sum

--- After rate change to 15% ---
Invoice: 1,000,000 + 150,000 tax = 1,150,000 sum
Receipt: 500,000 + 75,000 tax = 575,000 sum
Payroll: 3,000,000 - 450,000 tax = 2,550,000 sum
```

**File:** `task_04.py`

