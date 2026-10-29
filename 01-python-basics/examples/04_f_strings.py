"""Build neat text with f-strings: expressions, decimals, width, alignment
and thousands separators, plus the older str.format() for comparison.

Run: python 04_f_strings.py
"""

student = "Meera"
maths = 78
science = 91.5
english = 84

# Any expression can go inside the braces.
print(f"{student} scored {maths + science + english} marks in total.")

# :.2f keeps two digits after the decimal point.
average = (maths + science + english) / 3
print(f"Average: {average}")
print(f"Average rounded: {average:.2f}")

# :, inserts thousands separators; :,.2f does both at once.
population = 29164578
budget = 1834500.5
print(f"Population: {population:,}")
print(f"Budget: {budget:,.2f}")

# A number after the colon is the width. Text is left aligned by default,
# numbers are right aligned. <, > and ^ force left, right and centre.
print()
print(f"{'Subject':<10}{'Marks':>8}")
print(f"{'Maths':<10}{maths:>8}")
print(f"{'Science':<10}{science:>8}")
print(f"{'English':<10}{english:>8}")
print(f"{'-' * 18}")
print(f"{'Centred':^18}")

# str.format() does the same job with {} placeholders. You will see it in
# older code, so it is worth recognising.
print()
print("{} is {} years old.".format("Ravi", 19))
print("{0} likes {1}. {1} is fun.".format("Ravi", "Python"))
print("Pi is about {:.3f}".format(3.14159265))
