"""Write multiples_of(k), an infinite generator, and take values from it with islice and break."""

from itertools import islice


def multiples_of(k):
    n = 1
    while True:
        yield k * n
        n += 1


print("First five:", list(islice(multiples_of(7), 5)))

for value in multiples_of(7):
    if value > 100:
        print("First above 100:", value)
        break
