"""Protect an object's data with private attributes, getters, setters and @property.

Shows public, protected and private attributes, name mangling, and a
BankAccount whose balance can be read through a property but changed
only through deposit() and withdraw(). Run: python 05_encapsulation_property.py
"""


class Person:
    def __init__(self, name, age):
        self.name = name              # public: anyone may use it
        self._nickname = name[:3]     # protected: internal by convention
        self.__age = age              # private: Python mangles the name

    @property
    def age(self):                    # read with person.age
        return self.__age

    @age.setter
    def age(self, value):             # assign with person.age = value
        if not 0 <= value <= 120:
            raise ValueError(f"age must be between 0 and 120, got {value}")
        self.__age = value


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):                # a getter without a setter: read-only
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError(f"cannot withdraw {amount}, balance is {self.__balance}")
        self.__balance -= amount


sita = Person("Sita", 21)
print("Public    :", sita.name)
print("Protected :", sita._nickname, "(works, but the underscore says keep out)")
print("Property  :", sita.age)
try:
    print(sita.__age)
except AttributeError as error:
    print("Private   : Error:", error)
print("Mangled   :", sita._Person__age, "(the real stored name)")

print("\nThe setter validates every assignment:")
sita.age = 22
print("New age   :", sita.age)
try:
    sita.age = 150
except ValueError as error:
    print("Error     :", error)

print("\nA read-only balance:")
account = BankAccount("Asha", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance   :", account.balance)
try:
    account.balance = 999999
except AttributeError:
    print("Assigning account.balance is refused: there is no setter")
try:
    account.withdraw(5000)
except ValueError as error:
    print("Error     :", error)
