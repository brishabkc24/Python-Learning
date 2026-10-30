"""Item and Cart classes: add and remove items, compute the total and show the cart."""


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def cost(self):
        return self.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return
        print("Not in cart:", name)

    def total(self):
        return sum(item.cost() for item in self.items)

    def show(self):
        print("Cart:")
        for item in self.items:
            print(f"  {item.name:<12} x {item.quantity} = {item.cost():8.2f}")
        print(f"Total: {self.total():.2f}")


cart = Cart()
cart.add_item(Item("Notebook", 50, 3))
cart.add_item(Item("Pen", 10, 5))
cart.add_item(Item("Backpack", 1200, 1))
cart.show()

cart.remove_item("Ruler")
cart.remove_item("Pen")
print(f"After removing Pen, total: {cart.total():.2f}")
