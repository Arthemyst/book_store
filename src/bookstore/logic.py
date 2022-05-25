import requests

from bookstore.exceptions import WrongDictKey, GoogleBooksRequestError
from bookstore.models import Book
from bookstore.constants import BASE_URL


def fetch_books_by_author(authors):

    r = requests.get(BASE_URL, params={"q": authors})

    if not r.ok:
        raise GoogleBooksRequestError(r.reason)
    books = r.json()
    return books["items"]


def is_book_author(author, book):
    author_matches = False
    book_authors = book.get("volumeInfo", {}).get("authors", [])
    for book_author in book_authors:
        if author in book_author:
            author_matches = True
            break
    return author_matches


def save_books_to_db(books, author):
    counter = 0
    for book in books:

        if not is_book_author(author, book):
            continue

        _, created = Book.objects.update_or_create(
            external_id=book.get("id"),
            defaults={
                "title": book.get("volumeInfo", {}).get("title"),
                "authors": book.get("volumeInfo", {}).get("authors"),
                "published_year": book.get("volumeInfo", {}).get("publishedDate", "")[
                    :4
                ],
                "thumbnail": book.get("volumeInfo", {})
                .get("imageLinks", {})
                .get("thumbnail"),
            },
        )
        if created:
            counter += 1

    return counter
