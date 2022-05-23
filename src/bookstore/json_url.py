import requests


def load_json():
    authors = "Hobbit"
    url = "https://www.googleapis.com/books/v1/volumes?q="
    r = requests.get(url + authors)
    books = r.json()
    counter = 0
    for book in books["items"]:
        print(f"External id: {book['id']}")
        print(f"Title: {book['volumeInfo']['title']}")
        print(f"Authors: {book['volumeInfo']['authors']}")
        print(f"Published date: {book['volumeInfo']['publishedDate']}")
        print(f"Link: {book['volumeInfo']['infoLink']}")
        print("-" * 30)
        counter += 1
    print(counter)


load_json()


def load_books():
    book_data = request.data
    part_url = "https://www.googleapis.com/books/v1/volumes?q="
    full_url = part_url + book_data["title"]
    r = ""
    while r == "":
        try:
            r = requests.get(full_url, json={"key1": "value1"})
            break
        except requests.exceptions.ConnectionError:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
    books = r.json()
    counter = 0
    for book in books["items"]:
        new_book = Book.objects.create(
            external_id=book["id"],
            title=book["volumeInfo"]["title"],
            authors=book["volumeInfo"]["authors"],
            published_year=book["volumeInfo"]["publishedDate"],
            thumbnail=book["volumeInfo"]["infoLink"],
        )
        new_book.save()
        # serializer = BookSerializer(new_book)
        counter += 1

    print(f"Books loaded: {counter}")


# load_books()
