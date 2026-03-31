# Bug count: ? (find them all)
# Topic: type hints, dataclasses, @property, __post_init__
# Give after: L09
#
# Scenario: A product inventory dataclass for an online store with
#           validation, computed properties, and a discount method.
#
# Expected output:
#   Product: Laptop HP | SKU: ELEC-001 | Price: 4,500,000 sum | Stock: 10
#   Discounted price (15%): 3,825,000.0 sum
#   In stock: True
#   Total value: 45,000,000 sum
#   Error: price must be positive
#   Error: stock cannot be negative

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Product:
    name: str
    sku: str
    price: float
    stock: int
    category: str = "General"
    tags: list = field(default_factory=list)  

    def __post_init__(self):
        if self.price < 0:  # BUG — should be <= 0
            raise ValueError("price must be positive")
        if self.stock < 0:
            raise ValueError("stock cannot be negative")

    @property
    def in_stock(self) -> bool:
        return self.stock > 0

    @property
    def total_value(self) -> float:
        return self.price * self.stock

    def apply_discount(self, percent: float) -> float:
        if percent <= 0 or percent >= 100:
            raise ValueError("percent must be between 0 and 100")
        return self.price * (percent / 100)  # BUG — this calculates the discount amount, not the discounted price

    def __str__(self) -> str:
        return (f"Product: {self.name} | SKU: {self.sku} | "
                f"Price: {self.price:,.0f} sum | Stock: {self.stock}")

laptop = Product(name="Laptop HP", sku="ELEC-001", price=4_500_000, stock=10)
print(laptop)
print(f"Discounted price (15%): {laptop.apply_discount(15):,} sum")
print(f"In stock: {laptop.in_stock}")
print(f"Total value: {laptop.total_value:,} sum")

try:
    bad_product = Product("Broken", "X-001", -100, 5)  # BUG — -100 should trigger the error but check __post_init__
except ValueError as e:
    print(f"Error: {e}")

try:
    bad_stock = Product("No Stock", "X-002", 50000, -1)
except ValueError as e:
    print(f"Error: {e}")

