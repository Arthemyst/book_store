from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookstore.filters import BookFilter
from bookstore.logic import fetch_books_by_author, save_books_to_db
from bookstore.models import Book
from bookstore.serializers import BookSerializer
from bookstore.exceptions import GoogleBooksRequestError


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

    if "authors" not in book_data:
        return Response({"error": "Please specify authors"}, status_code=404)

    try:
        books = fetch_books_by_author(book_data["authors"])
    except GoogleBooksRequestError as exc:
        return Response({"error": f"Google Books API returned {str(exc)}"})

    counter = save_books_to_db(books, book_data["authors"])

    return Response({"imported": counter})


@api_view(["GET"])
def api_spec(request):
    return Response({"info": {"version": "2022.05.16"}})
