class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = list()

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for book in self.books:
            if book == book:
                self.books.remove(book)
                return

    def search_books(self, search_string):
        result = list()

        for book in self.books:
            if (search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower()):
                result.append(book)

        return result
