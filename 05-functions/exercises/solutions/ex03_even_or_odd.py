"""Exercise 3: an is_even function used to print the even numbers from 1 to 10."""


def is_even(number):
    return number % 2 == 0


for number in range(1, 11):
    if is_even(number):
        print(number, end=" ")
print()
