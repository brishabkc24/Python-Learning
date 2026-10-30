"""BankAccount that refuses bad amounts and keeps a history of successful actions."""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Refused: amount must be positive")
            return
        self.balance += amount
        self.history.append(f"deposit {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Refused: amount must be positive")
            return
        if amount > self.balance:
            print(f"Refused: cannot withdraw {amount}, balance is {self.balance}")
            return
        self.balance -= amount
        self.history.append(f"withdraw {amount}")

    def show_history(self):
        print(f"History of {self.owner}:")
        for entry in self.history:
            print(" ", entry)
        print("Final balance:", self.balance)


account = BankAccount("Asha", 1000)
account.deposit(500)
account.withdraw(2000)
account.withdraw(300)
account.deposit(-50)
account.show_history()
