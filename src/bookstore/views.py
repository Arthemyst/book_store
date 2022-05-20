from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from bookstore.models import Book
from bookstore.serializers import BookSerializer


@csrf_exempt
def book_list(request):
    """
    List all code book, or create a new book.
    """
    if request.method == "GET":
        snippets = Book.objects.all()
        serializer = BookSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def book_detail(request, pk):
    """
    Retrieve, update or delete a code book.
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        book.delete()
        return HttpResponse(status=204)
