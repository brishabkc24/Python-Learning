"""Exercise 2: a temperature module with two conversion functions and a self-test under the main guard."""


def c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print("Self-test of the temperature module")
    print("c_to_f(100) =", c_to_f(100))
    print("f_to_c(32) =", f_to_c(32))
