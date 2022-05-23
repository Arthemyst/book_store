from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookstore.filters import BookFilter
from bookstore.logic import book_load, book_requests
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

    books = book_requests(book_data, part_url)

    counter = book_load(books)

    return Response({"imported": counter})


@api_view(["GET"])
def api_spec(request):
    return Response({"info": {"version": "2022.05.16"}})
