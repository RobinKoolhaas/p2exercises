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
        pass

    def search_books(self, search_string):
        pass
