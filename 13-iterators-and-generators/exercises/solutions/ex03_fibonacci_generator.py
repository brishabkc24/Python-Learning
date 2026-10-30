"""Write fibonacci_below(limit), a generator of Fibonacci numbers smaller than limit."""


def fibonacci_below(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print(list(fibonacci_below(50)))
