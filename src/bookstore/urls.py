from django.urls import path

from bookstore import views


urlpatterns = [
    path("books/", views.BookList.as_view()),
    path("books/<int:pk>/", views.BookDetail.as_view()),
    path("import/", views.book_import),
    path("api_spec/", views.api_spec),
]
