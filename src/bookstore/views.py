from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.response import Response

from bookstore.models import Book
from bookstore.serializers import BookSerializer


class BookFilter(filters.FilterSet):
    published_year = filters.RangeFilter()
    title = filters.CharFilter()
    acquired = filters.BooleanFilter()

    class Meta:
        model = Book
        fields = [
            "title",
            "authors",
            "published_year",
            "acquired",
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
