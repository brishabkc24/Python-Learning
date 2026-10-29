"""Exercise 7: a UserList subclass whose append accepts only integers."""

from collections import UserList


class IntList(UserList):
    def append(self, item):
        if not isinstance(item, int):
            print("rejected:", repr(item))
            return
        super().append(item)


numbers = IntList()
for value in [5, "six", 7, 2.5]:
    numbers.append(value)

print(numbers)
print("Sum:", sum(numbers))
