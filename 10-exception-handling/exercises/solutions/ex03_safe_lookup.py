"""Write get_item(data, key) that returns "missing" on IndexError or KeyError."""


def get_item(data, key):
    try:
        return data[key]
    except (IndexError, KeyError):
        return "missing"


colours = ["red", "green", "blue"]
ages = {"Aarav": 20, "Sita": 21}

print("colours[1] ->", get_item(colours, 1))
print("colours[5] ->", get_item(colours, 5))
print("ages['Sita'] ->", get_item(ages, "Sita"))
print("ages['Kiran'] ->", get_item(ages, "Kiran"))
