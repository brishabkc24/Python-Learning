"""Report whether a number is divisible by 3, by 5, by both or by neither."""

number = int(input("Enter a number: "))

# Test the "both" case first; otherwise "by 3 only" would catch 45 too.
if number % 3 == 0 and number % 5 == 0:
    print(number, "is divisible by 3 and 5")
elif number % 3 == 0:
    print(number, "is divisible by 3 only")
elif number % 5 == 0:
    print(number, "is divisible by 5 only")
else:
    print(number, "is divisible by neither")
