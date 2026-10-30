"""Control what print() shows, then add, change and delete attributes.

Without __str__ an object prints as a class name and an address.
__str__ gives readable text and __repr__ gives programmer text that
lists use. The last part adds, changes and deletes attributes and
deletes a whole object. Run: python 05_str_and_repr.py
"""


class Plain:
    def __init__(self, title):
        self.title = title


class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

    def __repr__(self):
        return f"Book('{self.title}', {self.year})"


plain = Plain("Sapiens")
print("Without __str__ :", plain)           # the address differs on every run

book = Book("Sapiens", 2011)
print("With __str__    :", book)
print("repr() gives    :", repr(book))
print("Inside a list   :", [book, Book("Clean Code", 2008)])

print("\nAdding, changing and deleting attributes:")
book.price = 20.0                           # a new attribute on this object only
book.year = 2015                            # change an existing attribute
print("Attributes now  :", vars(book))

del book.price                              # remove one attribute
print("Has price?      :", hasattr(book, "price"))
print("Still prints    :", book)

del book                                    # the name book no longer exists
try:
    print(book)
except NameError as error:
    print("After del       :", error)
