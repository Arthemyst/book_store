import pytest
import requests
import responses

from bookstore.exceptions import WrongDictKey
from bookstore.logic import book_requests


def test_wrong_key_in_dict_for_book_authors():
    part_url = "https://www.googleapis.com/books/v1/volumes"
    book_data = {"wrong_key": "wrong_value"}
    with pytest.raises(
        WrongDictKey, match="Wrong key value in dictionary (must be 'authors')"
    ):
        books = book_requests(book_data, part_url)
