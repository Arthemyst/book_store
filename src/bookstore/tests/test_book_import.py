import pytest
from bookstore.models import Book

from bookstore.logic import fetch_books_by_author, save_books_to_db
from .mockup_variables import author_valid, author_invalid


@pytest.mark.django_db
def test_import_books_by_author_valid():
    books = fetch_books_by_author(author_valid)
    response1 = save_books_to_db(books, author_valid)
    response2 = save_books_to_db(books, author_valid)
    assert response2 == 0
    book1 = Book.objects.get(title="Blask fantastyczny Swiat dysku")
    book2 = Book.objects.get(title="Ostatni kontynent")
    book3 = Book.objects.get(title="Nauka Świata Dysku")

    book1.delete()
    book2.delete()
    book3.delete()


def test_import_books_by_author_invalid():
    books = fetch_books_by_author(author_invalid)
    response = save_books_to_db(books, author_invalid)
    assert response == 0
