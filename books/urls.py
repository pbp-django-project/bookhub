from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path("", views.show_books, name='show-books'),
    path("json/", views.get_books, name="get-books"),
    path("add-books/", views.add_books, name="add-books"),
    
]