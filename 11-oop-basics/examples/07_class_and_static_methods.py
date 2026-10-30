"""Use instance methods, class methods and static methods together.

Temperature stores a value in Celsius. from_fahrenheit() is a class
method that builds an object a second way, is_freezing() is a static
helper, and a class attribute counts how many readings were created.
Run: python 07_class_and_static_methods.py
"""


class Temperature:
    readings_created = 0

    def __init__(self, celsius):
        self.celsius = celsius
        Temperature.readings_created += 1

    def to_fahrenheit(self):                         # instance method: uses self
        return self.celsius * 9 / 5 + 32

    def show(self):
        state = "freezing" if Temperature.is_freezing(self.celsius) else "above freezing"
        print(f"{self.celsius:6.1f} C = {self.to_fahrenheit():6.1f} F ({state})")

    @classmethod
    def from_fahrenheit(cls, fahrenheit):            # class method: cls is Temperature
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)                          # the same as Temperature(celsius)

    @classmethod
    def how_many(cls):                               # class method: reads class data
        return cls.readings_created

    @staticmethod
    def is_freezing(celsius):                        # static method: no self, no cls
        return celsius <= 0


morning = Temperature(-3)
noon = Temperature(24.5)
evening = Temperature.from_fahrenheit(68)

for reading in (morning, noon, evening):
    reading.show()

print("\nIs 5 C freezing?", Temperature.is_freezing(5))
print("Readings created:", Temperature.how_many())
