"""Check whether a year is a leap year.

Run: python 05_leap_year.py

The rule: a year is a leap year if it is divisible by 4, except that years
divisible by 100 are not leap years, unless they are also divisible by 400.
"""

# Version 1: nested ifs that follow the rule word by word.
year = 1900
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year (divisible by 400)")
        else:
            print(year, "is not a leap year (divisible by 100 but not 400)")
    else:
        print(year, "is a leap year (divisible by 4 but not 100)")
else:
    print(year, "is not a leap year (not divisible by 4)")

print()

# Version 2: the whole rule as one condition. The brackets make the two
# alternatives clear: "divisible by 4 but not by 100" or "divisible by 400".
year = 2000
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

year = 2023
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

print()

# A leap year has 366 days; a conditional expression picks the number.
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
days = 366 if is_leap else 365
print(f"{year} has {days} days")
