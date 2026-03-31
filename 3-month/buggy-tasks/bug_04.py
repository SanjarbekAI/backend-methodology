# Bug count: ? (find them all)
# Topic: threading, locks, race conditions
# Give after: L09
#
# Scenario: A ticket booking system where multiple threads simultaneously
#           try to book the last seats. Without proper locking, seats
#           get double-booked. Fix the race condition.
#
# Expected output (order may vary, but total booked must never exceed 5):
#   Thread-1 booked seat 1
#   Thread-2 booked seat 2
#   Thread-3 booked seat 3
#   Thread-4 booked seat 4
#   Thread-5 booked seat 5
#   Thread-6: Sorry, no seats available
#   Thread-7: Sorry, no seats available
#   Final seats available: 0
#   Total booked: 5

import threading
import time

class TicketSystem:
    def __init__(self, total_seats: int):
        self.total_seats = total_seats
        self.available = total_seats
        self.booked_count = 0
        # BUG — missing a lock

    def book_seat(self, thread_name: str):
        # BUG — no lock acquired here
        if self.available > 0:
            time.sleep(0.01)  # simulate DB delay — makes race condition visible
            self.available -= 1
            self.booked_count += 1
            print(f"{thread_name} booked seat {self.booked_count}")
        else:
            print(f"{thread_name}: Sorry, no seats available")
        # BUG — no lock released here


system = TicketSystem(5)
threads = []

for i in range(1, 8):
    t = threading.Thread(target=system.book_seat, args=(f"Thread-{i}",))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Final seats available: {system.available}")
print(f"Total booked: {system.booked_count}")
# If total_booked > 5, the race condition was not fixed

