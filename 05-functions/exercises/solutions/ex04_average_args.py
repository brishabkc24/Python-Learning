"""Exercise 4: an average function that accepts any number of values with *args."""


def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


print("average(10, 20, 30) =", average(10, 20, 30))
print("average(5) =", average(5))
print("average() =", average())
