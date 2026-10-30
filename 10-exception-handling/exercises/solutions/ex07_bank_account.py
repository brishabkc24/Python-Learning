"""A BankAccount with InvalidAmountError and InsufficientBalanceError, processing a list of operations."""


class InvalidAmountError(Exception):
    def __init__(self, amount):
        super().__init__(f"Amount must be positive, got {amount}")


class InsufficientBalanceError(Exception):
    def __init__(self, amount, balance):
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientBalanceError(amount, self.balance)
        self.balance -= amount


operations = [
    ("deposit", 500),
    ("withdraw", 200),
    ("withdraw", 1000),
    ("deposit", -50),
    ("withdraw", 300),
]

account = BankAccount(100)
for action, amount in operations:
    try:
        if action == "deposit":
            account.deposit(amount)
        else:
            account.withdraw(amount)
    except (InvalidAmountError, InsufficientBalanceError) as error:
        print(f"{action} {amount} -> error: {error}")
    else:
        print(f"{action} {amount} -> balance {account.balance}")
