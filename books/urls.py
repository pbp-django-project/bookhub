from django.urls import path
from . import views
from reviews.views import show_reviews

app_name = 'books'

urlpatterns = [
    path("", views.show_books, name='show-books'),
    path("book-json/", views.get_books, name="get-books"),
    path("add-books/", views.add_books, name="add-books"),
    path("search/", views.search_books, name='search-books'),
    path("search/", views.search_books, name='search-books'),
    path("userbook-json/", views.get_userbooks, name='get-userbooks'),
    path("reviews/<int:book_id>", show_reviews, name='show-reviews'),
]