"""Temperature with a validated celsius property and a read-only fahrenheit property."""


class Temperature:
    ABSOLUTE_ZERO = -273.15

    def __init__(self, celsius):
        self.celsius = celsius                 # goes through the setter below

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < Temperature.ABSOLUTE_ZERO:
            raise ValueError(f"{value} is below absolute zero")
        self.__celsius = value

    @property
    def fahrenheit(self):                      # computed, no setter: read-only
        return self.__celsius * 9 / 5 + 32


room = Temperature(22)
print(f"{room.celsius} C = {room.fahrenheit} F")

room.celsius = 30
print(f"{room.celsius} C = {room.fahrenheit} F")

try:
    room.celsius = -300
except ValueError as error:
    print("Error:", error)

try:
    room.fahrenheit = 100
except AttributeError:
    print("Error: fahrenheit is read-only")

print(f"Still {room.celsius} C")
