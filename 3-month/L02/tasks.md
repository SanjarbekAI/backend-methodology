# L24 Tasks — OOP: Inheritance & Polymorphism

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The vehicle fleet

**Scenario**
A logistics company manages a mixed fleet of vehicles. Each vehicle type has shared properties but moves and refuels differently. The dispatch system works with all vehicle types through a common interface.

**Your task**
- Create `Vehicle` base class: `brand`, `model`, `fuel_level` (0–100), methods `move()`, `refuel(amount)`, `status()`
- Create `Truck(Vehicle)`: overrides `move()` to include load capacity; adds `load_weight` attribute
- Create `Van(Vehicle)`: overrides `move()` with delivery-specific message; adds `max_packages`
- Create `Motorcycle(Vehicle)`: overrides `move()`; 50% faster fuel consumption
- Create 2 of each, move them all using a loop via polymorphism, print status for each

**Expected output**
```
[Toyota Truck] Hauling 8.5 tonnes. Fuel: 87%
[Ford Van] Delivering 12 packages. Fuel: 92%
[Honda Motorcycle] Speeding ahead. Fuel: 85%
```

**File:** `task_01.py`

---

## Task 2 — The payment gateway

**Scenario**
A fintech platform supports multiple payment methods. Each method has the same interface but different processing logic. The checkout system charges customers through whichever gateway is configured.

**Your task**
- Create `PaymentGateway` base class: `name`, `transaction_fee` (%), methods `process(amount) -> str`, `refund(amount) -> str`, `get_fee(amount) -> float`
- Create `CreditCardGateway(PaymentGateway)`: 2% fee, overrides `process`
- Create `MobileWalletGateway(PaymentGateway)`: 0.5% fee, overrides `process`
- Create `BankTransferGateway(PaymentGateway)`: 0% fee, overrides `process`
- Write `checkout(gateway: PaymentGateway, amount: float)` function that processes and prints a receipt
- Call `checkout` with all 3 gateways for the same amount

**Expected output**
```
[CreditCard] Processing 500,000 sum...
Fee:     10,000 sum
Total:   510,000 sum ✓

[MobileWallet] Processing 500,000 sum...
Fee:      2,500 sum
Total:   502,500 sum ✓

[BankTransfer] Processing 500,000 sum...
Fee:          0 sum
Total:   500,000 sum ✓
```

**File:** `task_02.py`

---

## Task 3 — The notification system

**Scenario**
A SaaS platform sends notifications through different channels. The system must support adding new channels without changing the notification dispatcher.

**Your task**
- Create `Notifier` base class with `send(recipient: str, message: str) -> None` and `channel_name` attribute
- Create `EmailNotifier`, `SMSNotifier`, `PushNotifier`, `SlackNotifier` — each overrides `send()` with channel-specific formatting
- Create a `LoggingMixin` class with a `log(message: str)` method (prints with timestamp)
- Create `LoggedEmailNotifier(LoggingMixin, EmailNotifier)` — uses multiple inheritance
- Write `broadcast(notifiers: list[Notifier], recipient: str, message: str)`
- Broadcast an order confirmation to all 4 channels

**Expected output**
```
[Email → ali@mail.com] Order #8842 confirmed. Total: 250,000 sum
[SMS → +998912345678] Order #8842 confirmed.
[Push → ali_device] Order #8842 confirmed.
[Slack → @ali] Order #8842 confirmed.
[2026-03-30 14:25] [Email → ali@mail.com] Logged.
```

**File:** `task_03.py`

---

## Task 4 — The shape area calculator

**Scenario**
A CAD application calculates areas and perimeters for geometric shapes. All shapes share a common interface but compute their measurements differently.

**Your task**
- Create `Shape` base class: `color`, abstract-style method `area() -> float`, `perimeter() -> float`, `describe() -> str`
- Create `Circle(Shape)`: radius → area = πr², perimeter = 2πr
- Create `Rectangle(Shape)`: width, height → standard formulas
- Create `Triangle(Shape)`: sides a, b, c → Heron's formula for area
- Create `RightTriangle(Triangle)`: inherits from Triangle with c calculated automatically
- Create 2 of each shape, put in a list, print describe() for all via polymorphism

**Expected output**
```
Circle (red): area=78.54 cm², perimeter=31.42 cm
Rectangle (blue): area=24.00 cm², perimeter=20.00 cm
Triangle (green): area=6.00 cm², perimeter=12.00 cm
```

**File:** `task_04.py`

---

## Task 5 — The employee hierarchy

**Scenario**
A company models its staff hierarchy. Different employee types have different pay calculation methods but share common HR functionality. The payroll system processes all employee types uniformly.

**Your task**
- Create `Employee` base class: `emp_id`, `name`, `department`, method `calculate_pay() -> float`, `generate_payslip() -> str`
- Create `SalariedEmployee(Employee)`: fixed `monthly_salary`
- Create `HourlyEmployee(Employee)`: `hourly_rate` × `hours_worked`; overtime (>160hrs/month) at 1.5×
- Create `CommissionEmployee(Employee)`: `base_salary` + `commission_rate` × `sales_amount`
- Create 2 of each, put all 6 in a list, call `generate_payslip()` via polymorphism

**Expected output**
```
=== Payslip: Rustam Nazarov [Salaried] ===
Monthly Pay: 7,500,000 sum

=== Payslip: Sara Karimova [Hourly] ===
Regular: 160h × 25,000 = 4,000,000
Overtime: 20h × 37,500 = 750,000
Total: 4,750,000 sum

=== Payslip: Bobur Toshmatov [Commission] ===
Base: 2,000,000 + Commission: 1,500,000 = 3,500,000 sum
```

**File:** `task_05.py`

