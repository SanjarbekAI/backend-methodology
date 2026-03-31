# L28 — Practice: OOP

## Project brief
You are building a **hotel reservation system** — a fully object-oriented CLI application that manages rooms, guests, and bookings. The system must apply every OOP concept from Month 3: classes, inheritance, encapsulation, abstract classes, and SOLID/DRY principles. This is the kind of domain model you would write for a real backend API.

---

## Requirements

1. `Room` hierarchy: `Room(ABC)` → `StandardRoom`, `DeluxeRoom`, `Suite` — each with different pricing logic
2. `Guest` class with encapsulated profile data and a booking history
3. `Booking` dataclass connecting a guest to a room with check-in/check-out dates
4. `Hotel` class that manages all rooms, guests, and bookings (SRP: only orchestrates)
5. Separate `PricingStrategy(ABC)` with `WeekdayPricing`, `WeekendPricing`, `SeasonalPricing` implementations (OCP)
6. `BookingRepository(ABC)` with `InMemoryBookingRepository` implementation (DIP)
7. Full CLI menu: Add Guest, View Rooms, Book Room, Check Out, View Guest History, View All Bookings

---

## Milestones

**Milestone 1 (0:00–0:30) — Domain model**
- Build `Room` abstract class and 3 concrete room types
- Build `Guest` class with `@property` for protected data
- Build `Booking` dataclass with date validation in `__post_init__`
- Test all three in isolation

**Milestone 2 (0:30–1:00) — Pricing & repository**
- Build `PricingStrategy` hierarchy (OCP)
- Build `BookingRepository` abstract class and `InMemoryBookingRepository`
- Add `__str__`, `__repr__` to all domain objects
- Test booking creation and retrieval

**Milestone 3 (1:00–1:30) — Hotel orchestration**
- Build `Hotel` class (SRP — only coordinates, no business logic)
- Implement room availability checking
- Implement check-in and check-out flows
- Test the full booking lifecycle

**Milestone 4 (1:30–2:00) — CLI & polish**
- Build the full menu loop in `main()`
- Add `if __name__ == "__main__":` guard
- Add `HotelReporter` (SRP) for all display operations
- Test end-to-end: add guest → book room → check out → view history

---

## Bonus challenges

1. **Discount system:** Add a `DiscountStrategy` (OCP) applied on top of room pricing: `MemberDiscount`, `LongStayDiscount` (7+ nights), `CorporateDiscount`.
2. **Overbooking guard:** Ensure a room cannot be double-booked for overlapping dates — check on every new booking.
3. **JSON persistence:** Save and load all guests and bookings from JSON on start/exit using the Repository pattern.

