"""Exercise 3: a Book namedtuple with _replace and _asdict."""

from collections import namedtuple

Book = namedtuple("Book", ["title", "year", "price"])

book = Book("Learning Python", 2021, 450)
print(book)
print("Title:", book.title)

discounted = book._replace(price=400)
print("Discounted:", discounted)
print("As dict:", discounted._asdict())
