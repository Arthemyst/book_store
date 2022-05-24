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


def book_load(books, x):
    counter = 0
    for book in books["items"]:
        book_dict = {}
        try:
            if x["author"] not in book["volumeInfo"]["authors"][0]:
                pass
            else:
                try:
                    book_dict["External_id"] = book["id"]
                except KeyError:
                    book_dict["External_id"] = "null"
                try:
                    book_dict["Title"] = book["volumeInfo"]["title"]
                except KeyError:
                    book_dict["Title"] = "null"
                try:
                    book_dict["Authors"] = book["volumeInfo"]["authors"]
                except KeyError:
                    book_dict["Authors"] = "null"
                try:
                    book_dict["Published date"] = book["volumeInfo"]["publishedDate"][
                        :4
                    ]
                except KeyError:
                    book_dict["Published date"] = "null"
                try:
                    book_dict["Thumbnail"] = book["volumeInfo"]["imageLinks"][
                        "thumbnail"
                    ]
                except KeyError:
                    book_dict["Thumbnail"] = "null"
                print(book_dict)
        except KeyError:
            pass

        """
        _, created = Book.objects.update_or_create(
            external_id=book_dict["External_id"],
            defaults={
                "title": book_dict['Title'],
                "authors": book_dict["authors"],
                "published_year": book_dict["Published date"],
                "thumbnail": book_dict["Thumbnail"],
            },
        )
        if created:
            counter += 1
        """
    return counter
