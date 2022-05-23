from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookstore.exceptions import WrongDictKey
from bookstore.filters import BookFilter
from bookstore.logic import book_requests
from bookstore.models import Book
from bookstore.serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(["POST"])
def book_import(request):
    book_data = request.data
    part_url = "https://www.googleapis.com/books/v1/volumes"
    try:
        books = book_requests(book_data, part_url)
    except KeyError as e:
        raise WrongDictKey("Wrong key value in dictionary (must be 'authors')")

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

    return Response({"imported": counter})


@api_view(["GET"])
def api_spec(request):
    return Response({"info": {"version": "2022.05.16"}})
