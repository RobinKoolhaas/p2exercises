class Book:
    def __init__(self, title: str, isbn: str):
        self.title = title
        self.isbn = isbn

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) > 0:
            self.__title = title
        else:
            raise RuntimeError('Invalid title')

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        if Book.__is_valid_isbn(isbn):
            self.__isbn = isbn
        else:
            raise RuntimeError('Invalid isbn')

    @staticmethod
    def __is_valid_isbn(isbn: str) -> bool:
        isbn = [int(char) for char in isbn if char.isdigit()]

        if len(isbn) != 13:
            return False

        for i in range(0, 13):
            if i % 2 != 0:
                isbn[i] = isbn[i] * 3

        return sum(isbn) % 10 == 0
