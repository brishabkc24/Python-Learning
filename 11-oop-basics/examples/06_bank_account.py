"""Model a bank account with deposit, withdraw and show methods.

withdraw() refuses to take out more than the balance, and every
successful action is remembered in a history list that belongs to
the account. Run: python 06_bank_account.py
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []                    # each account records its own actions

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.balance += amount
        self.history.append(f"deposit {amount}")
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        # Check the balance before touching it, so it never goes negative.
        if amount > self.balance:
            print(f"Cannot withdraw {amount}. Balance is only {self.balance}")
            return
        self.balance -= amount
        self.history.append(f"withdraw {amount}")
        print(f"Withdrew {amount}. Balance: {self.balance}")

    def show(self):
        print(f"\nAccount of {self.owner}")
        print(f"  Balance: {self.balance}")
        print(f"  History: {', '.join(self.history)}")


asha = BankAccount("Asha", 1000)
bibek = BankAccount("Bibek")                 # balance uses the default of 0

asha.deposit(500)
asha.withdraw(2000)
asha.withdraw(300)
asha.deposit(-50)

bibek.deposit(200)
bibek.withdraw(50)

asha.show()
bibek.show()
