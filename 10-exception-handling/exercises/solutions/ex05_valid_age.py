"""Ask for an age until the user types a whole number between 1 and 120."""

while True:
    answer = input("Enter your age: ")
    try:
        age = int(answer)
    except ValueError:
        print("Please type a whole number.")
        continue
    if 1 <= age <= 120:
        break
    print("Age must be between 1 and 120.")

print("Age accepted:", age)
