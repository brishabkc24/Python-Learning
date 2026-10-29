"""Exercise 5: use datetime to find a weekday, add days to a date and count days between dates."""

import datetime

birthday = datetime.date(2005, 8, 15)

print("Birthday:", birthday)
print("Weekday:", birthday.strftime("%A"))
print("100 days later:", birthday + datetime.timedelta(days=100))

new_year = datetime.date(2026, 1, 1)
print("Days from birthday to 2026-01-01:", (new_year - birthday).days)
