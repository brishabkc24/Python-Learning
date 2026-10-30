"""Person class with name and city and an introduce() method."""


class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def introduce(self):
        print(f"Hi, I am {self.name} from {self.city}.")


sita = Person("Sita", "Pokhara")
aarav = Person("Aarav", "Kathmandu")

sita.introduce()
aarav.introduce()
