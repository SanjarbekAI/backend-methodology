# L28 Tasks — Practice: OOP

Complete the tasks below. Create a `.py` file for each task.

---

## Task 1 — The hotel reservation system (main project)

**Scenario**
A boutique hotel needs a command-line reservation system. It must model rooms, guests, and bookings using full OOP with inheritance, encapsulation, abstract classes, and SOLID principles.

**Your task**
- Build the full hotel system as described in `lesson.md`
- Organize code into at least: `models.py` (domain classes), `repositories.py` (data layer), `services.py` (business logic), `main.py` (CLI)
- All OOP concepts from L23–L27 must be demonstrably applied
- The system must handle invalid inputs gracefully

**Expected flow**
```
=== Grand Python Hotel ===

1. Add Guest         5. View Guest History
2. View Rooms        6. View All Bookings
3. Book Room         7. Exit
4. Check Out

> 3
Guest ID: G-001
Room number: 102
Check-in (YYYY-MM-DD): 2026-04-05
Check-out (YYYY-MM-DD): 2026-04-08

Booking confirmed: BK-0001
Room 102 (Deluxe) — 3 nights — 1,350,000 sum
```

**File:** `main.py` (+ `models.py`, `repositories.py`, `services.py`)

---

## Task 2 — The vehicle rental system

**Scenario**
A car rental agency needs a standalone OOP module demonstrating all SOLID principles applied to a vehicle rental domain: abstract vehicles, pricing strategies, dependency injection, and a clean single-responsibility structure.

**Your task**
- `Vehicle(ABC)`: abstract `daily_rate() -> float`, `vehicle_type() -> str`, concrete `rental_cost(days) -> float`
- Concrete classes: `Economy`, `SUV`, `Luxury`, `ElectricCar` with different base rates
- `RentalPricingStrategy(ABC)` → `StandardPricing`, `InsurancePricing` (+20%), `CorporatePricing` (-15%)
- `RentalService` takes a `VehicleRepository` (ABC) via DIP
- `InMemoryVehicleRepository` implementation
- Demonstrate booking 4 vehicles with 2 different pricing strategies

**Expected output**
```
Economy × 3 days [Standard]:   180,000 sum
SUV × 5 days [Insurance]:      875,000 sum
Luxury × 2 days [Corporate]:   680,000 sum
Electric × 7 days [Standard]:  490,000 sum
```

**File:** `task_02.py`

