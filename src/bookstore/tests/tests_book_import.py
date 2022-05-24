import pytest

from bookstore.exceptions import WrongDictKey
from bookstore.logic import book_load, book_requests


def test_wrong_key_in_dict_for_book_authors():
    part_url = "https://www.googleapis.com/books/v1/volumes"
    book_data = {"wrong_key": "wrong_value"}
    with pytest.raises(
        WrongDictKey, match="Wrong key value in dictionary (must be 'authors')"
    ):
        books = book_requests(book_data, part_url)


def test_specific_books_load_to_check_get_or_create():
    part_url = "https://www.googleapis.com/books/v1/volumes"
    book_data = {"authors": "Sienkiewicz"}
    books = book_requests(book_data, part_url)
    counter1 = book_load(books, book_data)
    counter2 = book_load(books, book_data)
    assert len(counter1) == 1
    assert len(counter2) == 0
