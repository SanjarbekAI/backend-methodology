# Bug count: ? (find them all)
# Topic: if/elif/else, comparison operators, logical operators
# Give after: L06
#
# Scenario: A cinema ticket pricing system.
# Rules:
#   age < 5    → free
#   age 5-12   → 15,000 sum (child)
#   age 13-17  → 25,000 sum (teen)
#   age 18-64  → 40,000 sum (adult)
#   age >= 65  → 20,000 sum (senior)
# Expected output for age=10:  "Child ticket: 15,000 sum"
# Expected output for age=70:  "Senior ticket: 20,000 sum"
# Expected output for age=3:   "Free entry!"

age = 10

if age < 5:
    print("Free entry!")
elif age >= 5 and age <= 12:  # BUG
    price = 15000
    print(f"Child ticket: {price:,} sum")
elif age >= 13 or age <= 17:  # BUG
    price = 25000
    print(f"Teen ticket: {price:,} sum")
elif age >= 18 and age <= 64:
    price = 40000
    print(f"Adult ticket: {price:,} sum")
elif age > 65:  # BUG
    price = 20000
    print("Senior ticket: {price:,} sum")  # BUG
else:
    print("Invalid age")

