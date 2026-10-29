"""Show what a NameError looks like and how to fix it.

Run: python 04_name_error_fixed.py
"""

# The broken version of this script looked like this:
#
#     greeting = "Good morning"
#     print(greting)
#
# Running it printed a traceback that ended with the line:
#
#     NameError: name 'greting' is not defined. Did you mean: 'greeting'?
#
# The variable was spelled "greeting" when it was created and "greting"
# when it was used. Python treats those as two different names, and the
# second one was never given a value. The fix is to spell it the same way.

greeting = "Good morning"
print(greeting)

# Python can also report the error without stopping the program.
# The try/except block below catches the NameError and prints its message.
# You will learn this properly in the Exception Handling topic.
try:
    print(greting)
except NameError as error:
    print("Caught an error:", error)

print("The program carried on after the error.")
