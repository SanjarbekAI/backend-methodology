# L33 — Practice: Full Review

## Project brief
You are building **PyStore** — a complete command-line e-commerce backend system that integrates every concept from all 3 months of the course. This is your capstone project. It should feel like something you could put in a portfolio.

**PyStore** is a product catalog, order management, and reporting system with:
- A full OOP domain model (Month 3)
- Functional data processing utilities (Month 2)
- Robust I/O, error handling, and file persistence (Month 1)
- Async order processing, performance optimization, and context managers (Month 3 advanced)

---

## Requirements

### Domain model (Month 3 — OOP)
1. `Product(ABC)` hierarchy: `PhysicalProduct`, `DigitalProduct`, `SubscriptionProduct` — each with different shipping and pricing logic
2. `Customer` class with encapsulated profile, order history, and `@property` accessors
3. `Order` dataclass connecting customer, products, quantities, and status
4. `PricingEngine(ABC)` with `StandardPricing`, `DiscountPricing`, `MemberPricing` (OCP)
5. `OrderRepository(ABC)` + `JsonOrderRepository` (DIP)
6. SOLID throughout — each class has a single, clear responsibility

### Processing layer (Month 2 — Functions & Intermediate)
7. Generator to produce sequential order IDs
8. Decorator to log every state-changing operation
9. Comprehensions for all search, filter, and transform operations
10. Type hints on every function and method
11. RegEx validation for email and phone on customer creation
12. JSON serialization/deserialization for all persistence

### Core layer (Month 1 — Basics)
13. Full CLI menu with all operations
14. `try/except` error handling on all user input
15. File I/O: auto-load on startup, save on exit
16. `if __name__ == "__main__":` guard

### Advanced layer (Month 3 — Advanced)
17. Async order fulfillment simulation (payment → inventory → shipping) using `asyncio`
18. `ManagedSession` context manager wrapping each order transaction
19. `__slots__` on high-volume objects (`CartItem`, `OrderLine`)
20. `@lru_cache` on the pricing calculation for repeated product/tier combinations

---

## Milestones

**Milestone 1 (0:00–0:30) — Domain model**
- Build all domain classes with full OOP hierarchy
- All dataclasses with `__post_init__` validation
- `__str__` and `__repr__` on all objects
- Test domain model independently

**Milestone 2 (0:30–1:00) — Processing & persistence layer**
- Order ID generator
- Logging decorator applied to order creation, cancellation, fulfillment
- `JsonOrderRepository` — full save/load cycle
- RegEx-validated `Customer` creation
- Test full CRUD on orders

**Milestone 3 (1:00–1:30) — Async fulfillment & advanced features**
- `async def fulfill_order(order)` pipeline: `authorize_payment` → `reserve_inventory` → `dispatch_shipping`
- `ManagedSession` context manager for transaction safety
- Apply `__slots__` to `CartItem`
- Apply `@lru_cache` to `PricingEngine.calculate(product, tier)`
- Test async fulfillment for a batch of 5 orders concurrently

**Milestone 4 (1:30–2:00) — CLI integration & final polish**
- Full menu loop with all 8 operations: Browse Products, Add to Cart, Place Order, View Order, Cancel Order, Fulfill Orders (async), View Reports, Exit
- Robust error handling throughout
- Auto-load / auto-save
- Generate and print a sales report on exit

---

## Bonus challenges

1. **Search & filter CLI:** Add product search by name, category, and price range using comprehensions and a generator pipeline.
2. **Performance report:** On exit, print a stats panel: cache hit rate for pricing, total orders processed, average fulfillment time, peak memory usage.
3. **Export:** Add a "Export to CSV" option using Python's `csv` module that exports all orders with full customer and product details.

