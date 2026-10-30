"""
Demonstrates custom exceptions: a BankAccount whose withdraw() raises
InsufficientBalanceError or InvalidAmountError. Each class subclasses
Exception and has its own __init__ that builds the message.
Run: python 05_custom_exceptions_bank.py
"""


class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Amount must be positive, got {amount}")


class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}: balance is only {balance}")


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount


account = BankAccount("Asha", 5000)
requests = [1500, -200, 10000, 3500]

for amount in requests:
    try:
        account.withdraw(amount)
    except InvalidAmountError as error:
        print("Invalid:", error)
    except InsufficientBalanceError as error:
        shortfall = error.amount - error.balance
        print(f"Refused: {error} (short by {shortfall})")
    else:
        print(f"Withdrew {amount}, balance is now {account.balance}")

print("Final balance:", account.balance)
