# Bug count: ? (find them all)
# Topic: __slots__, lru_cache, performance patterns
# Give after: L09
#
# Scenario: A high-performance coordinate point class using __slots__
#           and a cached distance calculator.
#
# Expected output:
#   Point(3, 4)
#   Point(0, 0)
#   Distance from origin: 5.0
#   Distance from origin: 5.0   ← served from cache
#   Cache info: CacheInfo(hits=1, misses=1, maxsize=128, currsize=1)
#   Error: cannot set 'z' — __slots__ prevents unknown attributes
#   Memory used by 10000 Points with __slots__: less than without

import math
from functools import lru_cache

class Point:
    __slots__ = ["x", "y"]  # BUG — should use a tuple, not a list, for __slots__

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


@lru_cache(maxsize=128)
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


p1 = Point(3, 4)
p2 = Point(0, 0)
print(p1)
print(p2)

d = distance(p1.x, p1.y, p2.x, p2.y)
print(f"Distance from origin: {d}")

d_cached = distance(p1.x, p1.y, p2.x, p2.y)
print(f"Distance from origin: {d_cached}   ← served from cache")

print(f"Cache info: {distance.cache_info()}")

# Test __slots__ enforcement
try:
    p1.z = 10  # BUG — will this actually raise an error with the current __slots__ definition?
except AttributeError as e:
    print(f"Error: cannot set 'z' — __slots__ prevents unknown attributes")

# Memory demonstration
import sys
points_with_slots = [Point(i, i) for i in range(10_000)]
print(f"Memory used by 10000 Points with __slots__: {sys.getsizeof(points_with_slots[0])} bytes per object")

class PointNoSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

points_no_slots = [PointNoSlots(i, i) for i in range(10_000)]
print(f"Memory used by 10000 Points without __slots__: {sys.getsizeof(points_no_slots[0])} bytes per object")
# BUG — sys.getsizeof does NOT measure the full object size for classes with __dict__
# Students must explain: what is the correct way to compare memory usage?

