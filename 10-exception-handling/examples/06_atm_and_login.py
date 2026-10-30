"""
Demonstrates custom exceptions in two small systems: an ATM that raises
InvalidPinError, and a login that raises UserNotFoundError or
WrongPasswordError. All accounts, emails and passwords are fictional.
Run: python 06_atm_and_login.py
"""


class InvalidPinError(Exception):
    def __init__(self, attempts_left):
        self.attempts_left = attempts_left
        super().__init__(f"Wrong PIN, {attempts_left} attempt(s) left")


class UserNotFoundError(Exception):
    def __init__(self, email):
        super().__init__(f"No account for {email}")


class WrongPasswordError(Exception):
    def __init__(self, email):
        super().__init__(f"Wrong password for {email}")


class ATM:
    def __init__(self, pin, balance):
        self._pin = pin
        self.balance = balance
        self.attempts_left = 3

    def check_pin(self, pin):
        if pin != self._pin:
            self.attempts_left -= 1
            raise InvalidPinError(self.attempts_left)
        self.attempts_left = 3       # a correct PIN resets the counter


def login(users, email, password):
    if email not in users:
        raise UserNotFoundError(email)
    if users[email] != password:
        raise WrongPasswordError(email)
    return f"Welcome, {email}"


print("ATM demo")
atm = ATM(pin="4321", balance=2000)
for pin in ["1111", "0000", "4321"]:
    try:
        atm.check_pin(pin)
        print("  PIN accepted, balance:", atm.balance)
    except InvalidPinError as error:
        print(f"  {error}")

print("Login demo")
users = {"asha@example.com": "password123", "bibek@example.com": "secret456"}
attempts = [
    ("asha@example.com", "password123"),
    ("mina@example.com", "password123"),
    ("bibek@example.com", "wrong"),
]
for email, password in attempts:
    try:
        print(f"  {login(users, email, password)}")
    except UserNotFoundError as error:
        print(f"  Login failed: {error}")
    except WrongPasswordError as error:
        print(f"  Login failed: {error}")
