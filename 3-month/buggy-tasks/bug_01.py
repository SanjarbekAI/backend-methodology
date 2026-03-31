# Bug count: ? (find them all)
# Topic: classes, __init__, instance vs class variables, instance methods
# Give after: L05
#
# Scenario: A bank account system with deposits, withdrawals, and transfer.
#
# Expected output:
#   Account[ACC-001] Sardor: 1,000,000 sum
#   Account[ACC-002] Nilufar: 500,000 sum
#   After deposit: 1,500,000 sum
#   After withdrawal: 1,200,000 sum
#   Transfer 200,000 from Sardor to Nilufar...
#   Sardor: 1,000,000 sum | Nilufar: 700,000 sum
#   Total accounts created: 2

class BankAccount:
    total_accounts = 0

    def __init__(self, account_id: str, owner: str, balance: float = 0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        total_accounts += 1  # BUG

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def transfer(self, target, amount: float):
        self.withdraw(amount)
        target.deposit(amount)

    def __str__(self):
        return f"Account[{self.account_id}] {self.owner}: {self.balance:,} sum"


acc1 = BankAccount("ACC-001", "Sardor", 1_000_000)
acc2 = BankAccount("ACC-002", "Nilufar", 500_000)

print(acc1)
print(acc2)

acc1.deposit(500_000)
print(f"After deposit: {acc1.balance:,} sum")

acc1.withdraw(300_000)
print(f"After withdrawal: {acc1.balance:,} sum")

print(f"Transfer 200,000 from Sardor to Nilufar...")
acc1.transfer(acc2, 200_000)
print(f"Sardor: {acc1.balance:,} sum | Nilufar: {acc2.balance:,} sum")

print(f"Total accounts created: {BankAccount.total_accounts}")

