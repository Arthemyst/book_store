import pytest
from bookstore.models import Book

from bookstore.exceptions import WrongDictKey
from bookstore.logic import book_load, book_requests
from .mockup_variables import author_valid, author_invalid, json_input_valid


def test_wrong_key_in_dict_for_book_authors():
    part_url = "https://www.googleapis.com/books/v1/volumes"
    book_data = {"wrong_key": "wrong_value"}
    with pytest.raises(
        WrongDictKey, match="Wrong key value in dictionary (must be 'authors')"
    ):
        books = book_requests(book_data, part_url)


def test_import_books_by_author_valid():
    response1 = book_load(json_input_valid, author_valid)
    response2 = book_load(json_input_valid, author_valid)
    assert len(response1) == 1
    assert len(response2) == 0
    book = Book.objects.get(external_id="ti3Qbej5wg4C")
    book.delete()


def test_import_books_by_author_valid():
    response = book_load(json_input_valid, author_invalid)
    assert len(response) == 0
