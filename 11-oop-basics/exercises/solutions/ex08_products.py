"""Product class with a tax_rate class attribute, a static tax helper and a from_string class method."""


class Product:
    tax_rate = 13                                  # percent, shared by all products

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def stock_value(self):
        return self.price * self.stock

    @staticmethod
    def price_with_tax(price):
        return price + price * Product.tax_rate / 100

    @classmethod
    def from_string(cls, text):
        name, price, stock = text.split(",")
        return cls(name, float(price), int(stock))


products = [
    Product.from_string("Pen,10,100"),
    Product("Notebook", 50, 40),
    Product("Backpack", 1200, 20),
    Product.from_string("Pencil,5,0"),
]

for product in products:
    print(f"{product.name:<10} price {product.price:.2f}  "
          f"with tax {Product.price_with_tax(product.price):.2f}")

best = max(products, key=lambda product: product.stock_value())
print(f"Highest stock value: {best.name} ({best.stock_value():.2f})")

total_value = sum(product.stock_value() for product in products)
print(f"Total stock value: {total_value:.2f}")
