from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.response import Response
import requests
from rest_framework.parsers import JSONParser
from bookstore.serializers import BookSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from bookstore.models import Book
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time



class BookFilter(filters.FilterSet):
    published_year = filters.RangeFilter()
    title = filters.CharFilter()
    acquired = filters.BooleanFilter()

    class Meta:
        model = Book
        fields = [
            "title",
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

    def get_serializer(self, *args, **kwargs):
        kwargs["partial"] = True
        return super(BookDetail, self).get_serializer(*args, **kwargs)




class BookImportView(APIView):

    def post(self, request, *args, **kwargs):      
        book_data = request.data
        part_url = "https://www.googleapis.com/books/v1/volumes?q="
        full_url = part_url + book_data['title']
        r = ''
        while r == '':
            try:
                r = requests.get(full_url, json={"key1":"value1"})
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
        for book in books['items']:
            new_book = Book.objects.create(
                external_id=book['id'], 
                title=book['volumeInfo']['title'], 
                authors=book['volumeInfo']['authors'], 
                published_year=book['volumeInfo']['publishedDate'], 
                thumbnail=book['volumeInfo']['infoLink'])
            new_book.save()
            #serializer = BookSerializer(new_book)
            counter += 1

        return Response({"imported": counter})
            

        

