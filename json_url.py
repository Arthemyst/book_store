import requests


def load_json():
    authors = "Lego"
    url = "https://www.googleapis.com/books/v1/volumes?q="
    r = requests.get(url + authors)
    books = r.json()
    counter = 0
    for book in books["items"]:
        print(f"External id: {book['id']}")
        print(f"Title: {book['volumeInfo']['title']}")
        print(f"Authors: {book['volumeInfo']['authors']}")
        print(f"Published year: {book['volumeInfo']['publishedDate']}")
        print(f"thumbnail: {book['volumeInfo']['infoLink']}")
        print("-" * 30)
        counter += 1
    print(counter)


load_json()
