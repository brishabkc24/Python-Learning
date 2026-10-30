"""
Demonstrates generator functions: yield pauses the function and remembers
where it was, next() resumes it, and the whole thing is much shorter than
an iterator class. Also compares yield with return.
Run: python 03_generators_yield.py
"""


def countdown(start):
    print("  (generator started)")
    while start >= 1:
        yield start               # pause here and hand out a value
        start -= 1
    print("  (generator finished)")


print("Calling countdown(3) runs none of its code yet:")
gen = countdown(3)
print("  type:", type(gen).__name__)

print("First next():")
print("  got", next(gen))
print("Second next():")
print("  got", next(gen))
print("Third next():")
print("  got", next(gen))
print("Fourth next() raises StopIteration:")
try:
    next(gen)
except StopIteration:
    print("  StopIteration caught")

# A for loop handles next() and StopIteration for us.
print("For loop over countdown(2):")
for number in countdown(2):
    print("  got", number)


# return gives ONE value and ends the function.
def squares_with_return():
    return [1, 4, 9]


# yield gives MANY values, one at a time, and keeps its place in between.
def squares_with_yield():
    yield 1
    yield 4
    yield 9


print("return version:", squares_with_return())
print("yield version :", type(squares_with_yield()).__name__)
print("yield as list :", list(squares_with_yield()))
