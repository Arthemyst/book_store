from django_filters import rest_framework as filters

from bookstore.models import Book


class BookFilter(filters.FilterSet):
    published_year = filters.RangeFilter()
    title = filters.CharFilter(label="Title", lookup_expr="icontains")
    acquired = filters.BooleanFilter()
    authors = filters.CharFilter(label="Authors", lookup_expr="icontains")

    class Meta:
        model = Book
        fields = [
            "title",
            "published_year",
            "acquired",
            "authors",
        ]
