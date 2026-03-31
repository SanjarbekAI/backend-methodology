# # Bug count: ? (find them all)
# # Topic: dictionaries, user input, type conversion, try/except
# # Give after: L10
# #
# # Scenario: A pharmacy stock checker. The pharmacist types a medicine name
# #           and quantity needed. The program checks stock and reports availability.
# #
# # Expected output (input: "Paracetamol", 30):
# #   Paracetamol: 120 units in stock
# #   Requested: 30
# #   Status: Available
# #
# # Expected output (input: "Aspirin", 200):
# #   Aspirin: 50 units in stock
# #   Requested: 200
# #   Status: Insufficient stock (need 150 more)
# #
# # Expected output (input: "Ibuprofen", abc):
# #   Error: quantity must be a whole number
#
# stock = {
#     "Paracetamol": 120,
#     "Aspirin": 50,
#     "Amoxicillin": 80,
#     "Ibuprofen": 200
# }
#
# medicine = input("Enter medicine name: ")
# qty_input = input("Enter quantity needed: ")
#
# try:
#     quantity = float(qty_input)  # BUG — should be int, not float
# except valueError:  # BUG
#     print("Error: quantity must be a whole number")
#
# if medicine in stock:
#     available = stock[medicine]
#     print(f"{medicine}: {available} units in stock")
#     print(f"Requested: {quantity}")
#     if quantity =< available:  # BUG
#         print("Status: Available")
#     else:
#         shortage = quantity - available
#         print(f"Status: Insufficient stock (need {shortage} more)")
# else:
#     print(f"{medicine} not found in stock")  # BUG — this line is outside try/except but uses `quantity` which may not be defined
#
