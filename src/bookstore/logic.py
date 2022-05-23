import requests

from bookstore.exceptions import WrongDictKey


def book_requests(book_data, part_url):

    part_url = "https://www.googleapis.com/books/v1/volumes"
    try:
        r = requests.get(part_url, params={"q": book_data["authors"]})
    except KeyError as e:
        raise WrongDictKey("Wrong key value in dictionary (must be 'authors')")

    books = r.json()
    return books
