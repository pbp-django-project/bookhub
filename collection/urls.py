from django.urls import path
from . import views

app_name = 'collection'

urlpatterns = [
    path("", views.show_collection, name='show-collection'),
    path("json/", views.get_collection, name="get-collection"),
    path("add-collection/", views.add_collection, name="add-collection"),
    path("search/", views.search_collection, name='search-collection'),
]