import pytest
from book import Book


@pytest.mark.parametrize('title', [
    'The Hobbit',
    'War Games',
    'World War Z'
])
@pytest.mark.parametrize('isbn', [
    '978-0547928227',
    '9780440193876',
    '978 0 30 7346605'
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)

    assert book.title == title
    assert book.isbn == isbn


@pytest.mark.parametrize('isbn', [
    '978-0547928227',
    '9780440193876',
    '978 0 30 7346605'
])
def test_creation_with_invalid_title(isbn):
    with pytest.raises(RuntimeError):
        Book('', isbn)


@pytest.mark.parametrize('title', [
    'The Hobbit',
    'War Games',
    'World War Z'
])
@pytest.mark.parametrize('isbn', [
    '978-1779501126',
    '9780735611331',
    '978-1709571127',
    '978-1-77-950182-7',
    '97817795011271',
    '978073561131'
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)
