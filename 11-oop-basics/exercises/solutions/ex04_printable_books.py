"""Book class with __str__ for people and __repr__ for lists."""


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


books = [
    Book("The Hobbit", "J. R. R. Tolkien", 1937),
    Book("1984", "George Orwell", 1949),
    Book("Sapiens", "Yuval Noah Harari", 2011),
]

print(books[0])        # uses __str__
print(books)           # the list uses __repr__ for every item
