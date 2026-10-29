"""Print an aligned receipt for three items with a total line."""

notebook_price = 45.0
pen_price = 12.5
bag_price = 899.99
total = notebook_price + pen_price + bag_price

# <10 pads the name to 10 characters; >8.2f right aligns the price in 8.
print(f"{'Notebook':<10}{notebook_price:>8.2f}")
print(f"{'Pen':<10}{pen_price:>8.2f}")
print(f"{'Bag':<10}{bag_price:>8.2f}")
print("-" * 18)
print(f"{'Total':<10}{total:>8.2f}")
