"""
Demonstrates custom iterator classes with __iter__ and __next__:
Countdown counts from a start value down to 1, and EvenNumbers gives the
even numbers up to a limit.
Run: python 02_custom_iterators.py
"""


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self                 # the object is its own iterator

    def __next__(self):
        if self.current < 1:
            raise StopIteration     # tells the for loop to stop
        value = self.current
        self.current -= 1
        return value


class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.limit:
            raise StopIteration
        return self.current


print("Countdown from 5:")
for number in Countdown(5):
    print("  ", number)

print("Even numbers up to 10:", list(EvenNumbers(10)))

# The iterator remembers its position, so next() carries on from there.
evens = EvenNumbers(6)
print("First even :", next(evens))
print("Second even:", next(evens))
print("The rest   :", list(evens))
print("Used up    :", list(evens))
