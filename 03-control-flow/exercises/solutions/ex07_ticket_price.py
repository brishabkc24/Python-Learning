"""Print the ticket price for a visitor based on their age."""

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: 0 (free)")
elif 5 <= age <= 17:
    print("Ticket price: 50")
elif 18 <= age <= 59:
    print("Ticket price: 100")
else:
    print("Ticket price: 60")
