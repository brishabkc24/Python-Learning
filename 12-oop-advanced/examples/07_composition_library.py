"""Build a Library that contains Book objects and behaves like a container.

Composition (has-a): the Library stores Books in a list instead of
inheriting from anything. The dunder methods __len__, __getitem__,
__iter__ and __contains__ make len(), indexing, for loops and the in
operator work on the Library. Run: python 07_composition_library.py
"""


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []                       # a Library has-a list of Books

    def add_book(self, book):
        if book in self.books:                # uses Book.__eq__
            print("Already in the library:", book.title)
            return
        self.books.append(book)

    def __len__(self):                        # len(library)
        return len(self.books)

    def __getitem__(self, index):             # library[0]
        return self.books[index]

    def __iter__(self):                       # for book in library
        return iter(self.books)

    def __contains__(self, book):             # book in library
        return book in self.books

    def oldest(self):
        return min(self.books, key=lambda book: book.year)


library = Library("City Library")
library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(Book("The Hobbit", "J. R. R. Tolkien", 1937))
library.add_book(Book("Sapiens", "Yuval Noah Harari", 2011))
library.add_book(Book("1984", "George Orwell", 1949))      # a duplicate

print(f"\n{library.name} holds {len(library)} books:")
for book in library:
    print(" -", book)

print("\nFirst book :", library[0])
print("Last book  :", library[-1])
print("Oldest book:", library.oldest())
print("Is Sapiens here?", Book("Sapiens", "Yuval Noah Harari", 2011) in library)
print("Is Dune here?   ", Book("Dune", "Frank Herbert", 1965) in library)
