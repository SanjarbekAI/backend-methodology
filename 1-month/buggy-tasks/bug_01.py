# Bug count: ? (find them all)
# Topic: print(), variables, data types, string formatting
# Give after: L06
#
# Scenario: A cashier app that greets a customer and shows their receipt.
# Expected output:
#   Welcome, Sardor!
#   Item: Laptop
#   Price: 4,500,000 sum
#   Discount: 10%
#   Final price: 4,050,000.0 sum

costumer_name = "Sardor"  # BUG
item = "Laptop"
price = 4_500_000
discount_percent = 10

print("Welcome, " + costumer_name + "!")  # BUG
print("Item: " + item)
print(f"Price: {price:,} sum")
print("Discount: " + discount_percent + "%")  # BUG

discount_amount = price * discount_percent / 100
final_price = price - discount_discount_amount  # BUG

print(f"Final price: {final_price:,} sum")

