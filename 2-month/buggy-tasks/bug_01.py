# # Bug count: ? (find them all)
# # Topic: functions, default parameters, return values, scope
# # Give after: L05
# #
# # Scenario: A hotel room pricing calculator with seasonal rates.
# #
# # Expected output:
# #   Standard room, 3 nights, off-season: 450,000 sum
# #   Deluxe room, 5 nights, peak season: 1,750,000 sum
# #   Suite, 2 nights, off-season: 700,000 sum
#
# ROOM_PRICES = {
#     "standard": 150_000,
#     "deluxe": 250_000,  # BUG — should be 350_000 (but the bug is structural, read below)
#     "suite": 350_000,
# }
#
# def calculate_stay(room_type, nights, peak_season=False):
#     base_price = ROOM_PRICES[room_type]
#     if peak_season = True:  # BUG
#         total = base_price * nights * 1.0  # BUG — peak season multiplier should be 1.5, not 1.0... wait, read expected output
#     else:
#         total = base_price * nights
#     return total
#
# def format_bill(room_type, nights, peak_season=False):
#     total = calculate_stay(room_type, nights, peak_season)
#     season = "peak season" if peak_season else "off-season"
#     # BUG — missing return statement
#     print(f"{room_type.capitalize()} room, {nights} nights, {season}: {total:,} sum")
#
# result1 = format_bill("standard", 3)
# result2 = format_bill("deluxe", 5, True)
# result3 = format_bill("suite", 2, peak_season=False)
#
# print(result1)  # BUG — think about what format_bill actually returns
# print(result2)
# print(result3)
#
