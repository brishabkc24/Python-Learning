"""Distance class with __add__, __eq__, __lt__ and __str__ so + == < sorted() and sum() work."""


class Distance:
    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        return Distance(self.km + other.km)

    def __eq__(self, other):
        return self.km == other.km

    def __lt__(self, other):
        return self.km < other.km

    def __str__(self):
        return f"{self.km} km"

    def __repr__(self):
        return f"Distance({self.km})"


morning = Distance(5)
evening = Distance(3.5)

print("Morning + evening:", morning + evening)
print("Equal?            ", morning == Distance(5))
print("Evening shorter?  ", evening < morning)
print("Longest:          ", max(morning, evening, Distance(12)))
print("Sorted:           ", sorted([morning, Distance(12), evening]))
# sum() starts from 0 by default, so give it a Distance to start from instead
print("Weekly total:     ", sum([morning, evening, Distance(12)], Distance(0)))
