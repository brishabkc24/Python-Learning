"""
The four kinds of functions, sorted by whether they take arguments and
whether they return a value. Each kind is shown with a tiny example and a
note on when it is the right choice.

Run: python 02_four_kinds.py
"""


# Kind 1: no arguments, no return value.
# Good for fixed actions such as printing a banner.
def show_banner():
    print("=" * 30)
    print("   Student Marks Report")
    print("=" * 30)


# Kind 2: no arguments, with a return value.
# Good for values that are computed or looked up, not passed in.
def get_pass_mark():
    return 40


# Kind 3: arguments, no return value.
# Good for displaying something built from the arguments.
def show_result(name, marks):
    status = "pass" if marks >= get_pass_mark() else "fail"
    print(name, "scored", marks, "->", status)


# Kind 4: arguments, with a return value.
# The most common and most reusable kind.
def average(marks_list):
    return sum(marks_list) / len(marks_list)


show_banner()
print("Pass mark is", get_pass_mark())
show_result("Sita", 92)
show_result("Rohan", 38)

class_average = average([92, 38, 67, 85])
print("Class average:", class_average)
show_result("Average student", class_average)
