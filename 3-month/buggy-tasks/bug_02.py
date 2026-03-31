# Bug count: ? (find them all)
# Topic: inheritance, super(), method overriding, polymorphism
# Give after: L05
#
# Scenario: A vehicle rental system with a base Vehicle class
#           and specialized Car and ElectricCar subclasses.
#
# Expected output:
#   Toyota Camry (2022) — Fuel: petrol — Rate: 150,000/day
#   Rental cost for 3 days: 450,000 sum
#   Tesla Model 3 (2023) — Fuel: electric — Battery: 80% — Rate: 200,000/day
#   Rental cost for 3 days: 600,000 sum
#   Charging cost for 50 kWh: 25,000 sum
#   Vehicles in fleet: 2

class Vehicle:
    fleet_count = 0

    def __init__(self, brand: str, model: str, year: int, daily_rate: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        Vehicle.fleet_count += 1

    def rental_cost(self, days: int) -> float:
        return self.daily_rate * days

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) — Rate: {self.daily_rate:,}/day"


class Car(Vehicle):
    def __init__(self, brand, model, year, daily_rate, fuel_type="petrol"):
        super().__init__(brand, model, year, daily_rate)
        self.fuel_type = fuel_type

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) — Fuel: {self.fuel_type} — Rate: {self.daily_rate:,}/day"


class ElectricCar(Car):
    def __init__(self, brand, model, year, daily_rate, battery_pct=100):
        super().__init__(brand, model, year, daily_rate, fuel_type="electric")
        self.battery_pct = battery_pct

    def charging_cost(self, kwh: float) -> float:
        return kwh * 500   # 500 sum per kWh

    def __str__(self):
        base = super.__str__()  # BUG
        return f"{base} — Battery: {self.battery_pct}%"


camry = Car("Toyota", "Camry", 2022, 150_000)
tesla = ElectricCar("Tesla", "Model 3", 2023, 200_000, battery_pct=80)

print(camry)
print(f"Rental cost for 3 days: {camry.rental_cost(3):,} sum")

print(tesla)
print(f"Rental cost for 3 days: {tesla.rental_cost(3):,} sum")
print(f"Charging cost for 50 kWh: {tesla.charging_cost(50):,} sum")

print(f"Vehicles in fleet: {Vehicle.fleet_count}")

# Polymorphism check
fleet = [camry, tesla]
for v in fleet:
    cost = v.rental_cost(3)  # BUG — not a code bug; add a comment: why does this work for both types?

