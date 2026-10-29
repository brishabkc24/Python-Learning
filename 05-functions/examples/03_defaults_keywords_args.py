"""
Default parameters, keyword arguments, *args and **kwargs, shown with a
temperature converter and a flexible order printer.

Run: python 03_defaults_keywords_args.py
"""


def convert_temperature(value, from_unit="C", to_unit="F"):
    """Convert between Celsius (C) and Fahrenheit (F)."""
    if from_unit == to_unit:
        return value
    if from_unit == "C":
        return value * 9 / 5 + 32
    return (value - 32) * 5 / 9


# Defaults: only the value is required.
print("25 C ->", convert_temperature(25), "F")

# Keyword arguments make the call readable and order-free.
print("98.6 F ->", convert_temperature(98.6, from_unit="F", to_unit="C"), "C")
print("10 C ->", convert_temperature(to_unit="C", value=10, from_unit="C"), "C")


def print_order(customer, *items, **options):
    """*items collects extra positional arguments into a tuple,
    **options collects extra keyword arguments into a dict."""
    print("Order for", customer)
    for item in items:
        print("  -", item)
    for option_name, option_value in options.items():
        print("  option:", option_name, "=", option_value)
    print("  items:", len(items), "| options:", len(options))


print_order("Sita", "tea", "samosa")
print_order("Aarav", "coffee", "cake", "water", delivery=True, tip=50)
print_order("Nabin")


def total(*numbers):
    """Add any number of values."""
    return sum(numbers)


print("total() =", total())
print("total(5) =", total(5))
print("total(1, 2, 3, 4) =", total(1, 2, 3, 4))

# A star also unpacks a list into separate arguments.
prices = [120, 80, 45]
print("total(*prices) =", total(*prices))
