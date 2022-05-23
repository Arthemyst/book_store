import requests

from bookstore.exceptions import WrongDictKey
from bookstore.models import Book


def book_requests(book_data, part_url):

    try:
        r = requests.get(part_url, params={"q": book_data["authors"]})
    except KeyError as e:
        raise WrongDictKey("Wrong key value in dictionary (must be 'authors')")

    books = r.json()
    return books


def book_load(books):
    counter = 0
    for book in books["items"]:
        try:

            _, created = Book.objects.update_or_create(
                external_id=book["id"],
                defaults={
                    "title": book["volumeInfo"]["title"],
                    "authors": book["volumeInfo"]["authors"],
                    "published_year": book["volumeInfo"]["publishedDate"][:4],
                    "thumbnail": book["volumeInfo"]["imageLinks"]["thumbnail"],
                },
            )
            if created:
                counter += 1
        except KeyError:
            continue
    return counter
