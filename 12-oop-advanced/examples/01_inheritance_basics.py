"""Inherit from a parent class, extend __init__ with super() and override a method.

Animal is the parent. Dog reuses everything from Animal, adds a trick
attribute through super().__init__(), overrides speak() and still calls
the parent's version with super(). Run: python 01_inheritance_basics.py
"""


class Animal:
    def __init__(self, name, legs=4):
        self.name = name
        self.legs = legs

    def speak(self):
        print(f"{self.name} makes a sound")

    def describe(self):
        print(f"{self.name} has {self.legs} legs")


class Dog(Animal):                       # Dog is-a Animal
    def __init__(self, name, trick):
        super().__init__(name)           # let Animal set name and legs first
        self.trick = trick               # then add what only dogs have

    def speak(self):                     # overrides Animal.speak
        super().speak()                  # keep the parent's behaviour...
        print(f"{self.name} says Woof!")  # ...and add the dog's own

    def perform(self):
        print(f"{self.name} can {self.trick}")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, legs=2)


generic = Animal("Nemo")
buddy = Dog("Buddy", "roll over")
tweety = Bird("Tweety")

print("Parent object:")
generic.speak()
generic.describe()

print("\nChild object (Dog):")
buddy.speak()
buddy.describe()                         # inherited, not written in Dog
buddy.perform()

print("\nAnother child (Bird):")
tweety.speak()
tweety.describe()

print("\nChecking relationships:")
print("buddy is a Dog?             ", isinstance(buddy, Dog))
print("buddy is an Animal?         ", isinstance(buddy, Animal))
print("tweety is a Dog?            ", isinstance(tweety, Dog))
print("Dog is a subclass of Animal?", issubclass(Dog, Animal))
