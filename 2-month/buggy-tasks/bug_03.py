# Bug count: ? (find them all)
# Topic: closures, decorators, generators
# Give after: L05
#
# Scenario: An e-commerce discount engine with logging and a product price generator.
#
# Expected output:
#   [LOG] calling apply_discount
#   Price after 20% discount: 800000
#   [LOG] calling apply_discount
#   Price after 5% discount: 950000
#   Generating prices...
#   100000
#   200000
#   300000
#   400000
#   500000

import functools

# --- Decorator ---
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] calling {func.__name__}")
        result = func(*args, *kwargs)  # BUG
        return result
    return wrapper

# --- Closure ---
def make_discount(rate):
    def apply(price):
        return price * (1 - rate)
    return apply  # BUG — returns the inner function, but read the usage below

@logger
def apply_discount(price, discount_func):
    return int(discount_func(price))

discount_20 = make_discount(0.20)
discount_05 = make_discount(0.05)

print("Price after 20% discount:", apply_discount(1_000_000, discount_20))
print("Price after 5% discount:", apply_discount(1_000_000, discount_05))

# --- Generator ---
def price_generator(start, stop, step):
    current = start
    while current < stop:
        yield current
        current = current + step

print("Generating prices...")
gen = price_generator(100_000, 600_000, 100_000)
for price in gen:
    print(price)

# This should print nothing (generator exhausted) — but student must explain why:
print("Remaining:", list(gen))  # BUG — not a code bug, but add a comment explaining the output

