# Bug count: ? (find them all)
# Topic: *args, **kwargs, lambda, map(), filter()
# Give after: L05
#
# Scenario: A payroll system that calculates net salaries with deductions.
#
# Expected output:
#   Gross salaries: [5000000, 7500000, 3200000, 8800000, 4100000]
#   After 12% tax: [4400000.0, 6600000.0, 2816000.0, 7744000.0, 3608000.0]
#   High earners (above 5,000,000 gross): [7500000, 8800000]
#   Total payroll after tax: 25168000.0
#   Bonus for Aziz: 750000.0
#   Bonus for Barno: 1125000.0

salaries = [5_000_000, 7_500_000, 3_200_000, 8_800_000, 4_100_000]

# Apply 12% tax deduction using lambda + map
after_tax = list(map(lambda s: s * 0.88, salaries))  
print("Gross salaries:", salaries)
print("After 12% tax:", after_tax)

# Filter high earners (gross above 5,000,000)
high_earners = list(filter(lambda s: s > 5_000_000, after_tax))  # BUG — should filter from original salaries
print("High earners (above 5,000,000 gross):", high_earners)

# Sum using reduce
from functools import reduce
total = reduce(lambda a, b: a + b, after_tax)
print(f"Total payroll after tax: {total}")

# Bonus calculator using *args and **kwargs
def calculate_bonus(*employee_names, rate=0.10, **salary_map):
    for name in employee_names:
        if name in salary_map:
            bonus = salary_map[name] * rate
            print(f"Bonus for {name}: {bonus}")

calculate_bonus("Aziz", "Barno", rate=0.15, Aziz=5_000_000, Barno=7_500_000, Jasur=3_200_000)
# BUG — the call above produces correct output, but below call is wrong:
calculate_bonus("Kamola", 0.10, Kamola=4_100_000)  # BUG — 0.10 is not a keyword arg

