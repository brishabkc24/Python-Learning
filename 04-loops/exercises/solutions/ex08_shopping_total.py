"""Read prices until 0 is entered, then print the item count and the total."""

item_count = 0
total = 0.0

while True:
    price = float(input("Enter a price (0 to finish): "))
    if price == 0:
        break
    item_count += 1
    total += price

print("Items:", item_count)
print(f"Total: {total:.2f}")
