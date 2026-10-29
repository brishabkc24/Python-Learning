"""Exercise 7: a recursive function that adds up the digits of a positive integer."""


def sum_of_digits(number):
    if number < 10:
        return number
    return number % 10 + sum_of_digits(number // 10)


print("sum_of_digits(4729) =", sum_of_digits(4729))
print("sum_of_digits(10000) =", sum_of_digits(10000))
