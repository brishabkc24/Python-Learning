"""Validate phone numbers that start with 98 or 97 and have 10 digits in total."""

import re

numbers = ["9801234567", "9741234567", "9601234567", "980123456", "98012345678"]

for number in numbers:
    status = "valid" if re.fullmatch(r"^(98|97)\d{8}$", number) else "invalid"
    print(number, status)
