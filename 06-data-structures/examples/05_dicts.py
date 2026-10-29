"""
Dictionaries: creating, safe lookup with get(), adding, updating and
deleting keys, looping over keys/values/items, a nested dictionary and
building a dictionary from zip or from a list of tuples.

Run: python 05_dicts.py
"""

prices = {"tea": 20, "coffee": 50, "samosa": 25}
print("prices:", prices)

# [] raises KeyError for a missing key; get() returns None or a default.
print("tea costs:", prices["tea"])
print("get('cake'):", prices.get("cake"))
print("get('cake', 0):", prices.get("cake", 0))

# Add, update, delete.
prices["cake"] = 80
prices["tea"] = 25
prices.update({"water": 15, "coffee": 55})
del prices["samosa"]
removed_price = prices.pop("water")
print("after changes:", prices, "| popped:", removed_price)

# Looping: keys by default, or values, or both with items().
for item in prices:
    print(" key:", item)
for price in prices.values():
    print(" value:", price)
for item, price in prices.items():
    print(" ", item, "costs", price)
print("total of all prices:", sum(prices.values()))
print("most expensive:", max(prices, key=prices.get))

# Nested dictionary: one record per student.
students = {
    "s1": {"name": "Sita", "city": "Pokhara", "marks": 92},
    "s2": {"name": "Aarav", "city": "Kathmandu", "marks": 85},
}
students["s3"] = {"name": "Bikash", "city": "Lalitpur", "marks": 67}
students["s2"]["marks"] = 90
for student_id, info in students.items():
    print(student_id, "->", info["name"], "from", info["city"], "scored", info["marks"])

# Building dictionaries from other data.
names = ["Sita", "Aarav", "Bikash"]
ages = [21, 20, 19]
print("from zip:", dict(zip(names, ages)))

pairs = [("red", "#FF0000"), ("green", "#00FF00"), ("blue", "#0000FF")]
print("from pairs:", dict(pairs))

# Counting with a dictionary: the classic pattern.
letter_count = {}
for letter in "banana":
    letter_count[letter] = letter_count.get(letter, 0) + 1
print("letters in 'banana':", letter_count)
