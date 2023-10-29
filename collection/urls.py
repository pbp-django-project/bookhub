from django.urls import path
from . import views

app_name = 'collection'

urlpatterns = [
    path("", views.show_collection, name='show-collection'),
    path("json/<int:id>", views.get_collection, name="get-collection"),
    path("add-collection/", views.add_collection, name="add-collection"),
    path("search/", views.search_collection, name='search-collection'),
    path('delete/<int:id>', views.delete_collection, name='delete'),
    path('edit/<int:pk>/', views.edit_book, name='edit-book'),
]