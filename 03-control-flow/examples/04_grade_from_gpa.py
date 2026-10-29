"""Turn a GPA (0.0 to 4.0) into a letter grade using ranges, and show
how a comparison chain such as 3.0 <= gpa < 3.6 reads naturally.

Run: python 04_grade_from_gpa.py
"""

gpa = 3.2
print("GPA:", gpa)

# Each test is a range. The chain 3.0 <= gpa < 3.6 means
# "gpa is at least 3.0 and less than 3.6". Out-of-range values are
# rejected first so that a typing mistake such as 7.5 is not graded.
if gpa > 4.0 or gpa < 0.0:
    grade = "invalid"
elif 3.6 <= gpa <= 4.0:
    grade = "A"
elif 3.0 <= gpa < 3.6:
    grade = "B"
elif 2.0 <= gpa < 3.0:
    grade = "C"
else:
    grade = "D"
print("Grade (full ranges):", grade)

# Because elif only runs when the earlier tests failed, the lower bound of
# each range is already guaranteed. This shorter version gives the same
# answer and is the style most Python programmers use.
if gpa > 4.0 or gpa < 0.0:
    grade = "invalid"
elif gpa >= 3.6:
    grade = "A"
elif gpa >= 3.0:
    grade = "B"
elif gpa >= 2.0:
    grade = "C"
else:
    grade = "D"
print("Grade (short form):", grade)

print()

# The same short form with a different value, to show another branch.
gpa = 1.9
print("GPA:", gpa)
if gpa > 4.0 or gpa < 0.0:
    grade = "invalid"
elif gpa >= 3.6:
    grade = "A"
elif gpa >= 3.0:
    grade = "B"
elif gpa >= 2.0:
    grade = "C"
else:
    grade = "D"
print("Grade (short form):", grade)

# A conditional expression is handy for a yes/no detail such as honours.
honours = "with honours" if gpa >= 3.6 else "without honours"
print("Result:", honours)
