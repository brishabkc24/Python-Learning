"""Exercise 3: import the temperature module from exercise 2 and convert a few values."""

import ex02_temperature

for celsius in [0, 25, 37]:
    print(celsius, "C =", ex02_temperature.c_to_f(celsius), "F")

print("98.6 F =", round(ex02_temperature.f_to_c(98.6), 1), "C")
print("module name:", ex02_temperature.__name__)
