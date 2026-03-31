# Bug count: ? (find them all)
# Topic: context managers (__enter__, __exit__, contextlib)
# Give after: L09
#
# Scenario: A database connection simulator and a timed execution context manager.
#           Both must properly clean up resources even when exceptions occur.
#
# Expected output:
#   [DB] Connection opened to mydb
#   [DB] Executing: SELECT * FROM users
#   [DB] Executing: SELECT * FROM products
#   [DB] Connection closed
#   [TIMER] finished in X.XXXs
#   [DB] Connection opened to mydb
#   [DB] Executing: DROP TABLE users
#   [DB] Error caught: Operation not permitted
#   [DB] Connection closed
#   Done

import time
from contextlib import contextmanager

class DatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        print(f"[DB] Connection opened to {self.db_name}")
        self.connected = True
        return self   # BUG — this is actually correct; students must identify what IS wrong below

    def execute(self, query: str):
        if not self.connected:
            raise RuntimeError("Not connected")
        print(f"[DB] Executing: {query}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        if exc_type is not None:
            print(f"[DB] Error caught: {exc_val}")
        print(f"[DB] Connection closed")
        return True  # BUG — this silently suppresses ALL exceptions including unexpected ones


@contextmanager
def timer(label="operation"):
    start = time.time()
    yield  # BUG — should yield something useful, or is this fine? students must decide and explain
    end = time.time()
    # BUG — missing the print statement for the timer result


with timer("database queries"):
    with DatabaseConnection("mydb") as db:
        db.execute("SELECT * FROM users")
        db.execute("SELECT * FROM products")

with DatabaseConnection("mydb") as db:
    db.execute("DROP TABLE users")
    raise PermissionError("Operation not permitted")  # BUG — will __exit__ handle this?

print("Done")

