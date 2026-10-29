"""Read two values with input() and convert them before doing arithmetic.

Run: python 02_input_and_casting.py

Sample session:
    Enter your age: 20
    Enter your height in metres: 1.75
    input() gave us: '20' -> <class 'str'>
    After int(): 20 -> <class 'int'>
    Next year you will be 21
    Your height is 1.75 metres, which is 175.0 cm
    Height as text: '1.75' -> <class 'str'>
"""

# input() always returns a string, even when the user types digits.
age_text = input("Enter your age: ")
height_text = input("Enter your height in metres: ")

print(f"input() gave us: '{age_text}' -> {type(age_text)}")

# int() converts text made of digits into a whole number.
age = int(age_text)
print(f"After int(): {age} -> {type(age)}")

# Now arithmetic works. With the string, age_text + 1 would be a TypeError.
print("Next year you will be", age + 1)

# float() handles numbers with a decimal point.
height = float(height_text)
print(f"Your height is {height} metres, which is {height * 100} cm")

# str() goes the other way: number to text. Useful when joining with + .
height_again = str(height)
print(f"Height as text: '{height_again}' -> {type(height_again)}")
