import requests
from django.utils.safestring import mark_safe
from django_filters import rest_framework as filters
from django_filters.fields import DateRangeField
from django_filters.filters import RangeFilter
from django_filters.widgets import RangeWidget
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookstore.models import Book
from bookstore.serializers import BookSerializer


class BookFilter(filters.FilterSet):
    published_year = filters.RangeFilter()
    title = filters.CharFilter()
    acquired = filters.BooleanFilter()
    authors = filters.CharFilter()

    class Meta:
        model = Book
        fields = [
            "title",
            "published_year",
            "acquired",
            "authors",
        ]


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter

    def get_paginated_response(self, data):
        return Response(data)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs["partial"] = True
        return super(BookDetail, self).get_serializer(*args, **kwargs)


@api_view(["POST"])
def book_import(request):
    book_data = request.data
    part_url = "https://www.googleapis.com/books/v1/volumes?q="
    full_url = part_url + book_data["title"]
    r = requests.get(full_url, json={"key1": "value1"})

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

    return Response({"imported": counter})


@api_view(["GET"])
def api_spec(request):
    return Response({"info": {"version": "2022.05.16"}})
