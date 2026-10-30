"""Abstract Payment class with pay() implemented by CardPayment, CashPayment and WalletPayment."""

from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, customer):
        self.customer = customer

    @abstractmethod
    def pay(self, amount):
        pass

    def receipt(self, amount):
        # Shared by every child; the child only decides how to pay.
        print(f"Receipt for {self.customer}: {amount:.2f} paid by {type(self).__name__}")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Charging {amount:.2f} to the card of {self.customer}")
        self.receipt(amount)


class CashPayment(Payment):
    def pay(self, amount):
        print(f"{self.customer} hands over {amount:.2f} in cash")
        self.receipt(amount)


class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Deducting {amount:.2f} from the wallet of {self.customer}")
        self.receipt(amount)


payments = [CardPayment("Asha"), CashPayment("Bibek"), WalletPayment("Deepa")]
for payment in payments:
    payment.pay(1250)

try:
    Payment("Nobody")
except TypeError as error:
    print("Error:", error)
