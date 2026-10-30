"""Define NegativeNumberError and a square_root() function that raises it for negative input."""


class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Cannot take the square root of {number}")


def square_root(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number ** 0.5


for value in [16, -4, 2.25]:
    try:
        print(f"square_root({value}) =", square_root(value))
    except NegativeNumberError as error:
        print("Error:", error)
