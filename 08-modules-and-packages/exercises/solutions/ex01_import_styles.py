"""Exercise 1: use the math module through three different import styles."""

import math
print("sqrt(144) =", math.sqrt(144))

import math as m
print("pi rounded =", round(m.pi, 3))

from math import factorial
print("factorial(6) =", factorial(6))
