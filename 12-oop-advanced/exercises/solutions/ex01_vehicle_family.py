"""Vehicle parent with Car and Bike children that set their own wheel count and call display()."""


class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def display(self):
        print(f"{type(self).__name__}: {self.brand} with {self.wheels} wheels")


class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand, 4)
        self.seats = seats

    def display(self):
        super().display()
        print(f"  seats: {self.seats}")


class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 2)


vehicles = [Car("Toyota", 5), Bike("Honda"), Car("Suzuki", 7)]
for vehicle in vehicles:
    vehicle.display()

total_wheels = sum(vehicle.wheels for vehicle in vehicles)
print("Total wheels:", total_wheels)
