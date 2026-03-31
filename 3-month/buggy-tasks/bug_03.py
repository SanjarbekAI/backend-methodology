# Bug count: ? (find them all)
# Topic: encapsulation, @property, magic methods (__str__, __len__, __eq__, __add__)
# Give after: L05
#
# Scenario: A shopping cart system with encapsulated total, item count magic methods,
#           cart equality comparison, and cart merging.
#
# Expected output:
#   Cart(Sardor): 3 items, total: 1,285,000 sum
#   Cart(Nilufar): 2 items, total: 920,000 sum
#   len(cart1) = 3
#   cart1 == cart1_copy: True
#   cart1 == cart2: False
#   Merged cart: 5 items, total: 2,205,000 sum

class ShoppingCart:
    def __init__(self, owner: str):
        self.owner = owner
        self.__items = []   # private

    def add_item(self, name: str, price: float):
        if price <= 0:
            raise ValueError("Price must be positive")
        self.__items.append({"name": name, "price": price})

    @property
    def total(self) -> float:
        return sum(item["price"] for item in self.__items)

    @property
    def items(self):
        return self.__items  # BUG — returns a mutable reference, should return a copy

    def __str__(self):
        return f"Cart({self.owner}): {len(self)} items, total: {self.total:,} sum"

    def __len__(self):
        return len(self.__items)

    def __eq__(self, other):
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        return self.total == other.total and len(self) == len(other)

    def __add__(self, other):
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        merged = ShoppingCart(f"{self.owner}+{other.owner}")
        for item in self.items:
            merged.add_item(item["name"], item["price"])
        for item in other.items:
            merged.add_item(item["name"], item["price"])
        return merged


cart1 = ShoppingCart("Sardor")
cart1.add_item("Keyboard", 350_000)
cart1.add_item("Mouse", 185_000)
cart1.add_item("Mousepad", 750_000)

cart2 = ShoppingCart("Nilufar")
cart2.add_item("Headphones", 620_000)
cart2.add_item("USB Hub", 300_000)

print(cart1)
print(cart2)
print(f"len(cart1) = {len(cart1)}")

cart1_copy = ShoppingCart("Sardor_copy")
cart1_copy.add_item("Keyboard", 350_000)
cart1_copy.add_item("Mouse", 185_000)
cart1_copy.add_item("Mousepad", 750_000)

print(f"cart1 == cart1_copy: {cart1 == cart1_copy}")
print(f"cart1 == cart2: {cart1 == cart2}")

merged = cart1 + cart2
print(f"Merged cart: {merged}")

# This should NOT modify cart1 — but will it? Check the items property bug:
cart1.items.append({"name": "HACKED", "price": 999})  # BUG — exposed because of the property bug above
print(f"cart1 after external append: {cart1}")  # if items is 4, the property bug is confirmed

