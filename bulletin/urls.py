from django.urls import path
from . import views

app_name = "bulletin"

urlpatterns = [
    path("", views.show_bulletin, name="show-bulletin"),
    path("add-bulletin/", views.add_news_page, name="add-news-page"),
    path("full-news/<int:bulletin_id>", views.show_full_news, name="full-news"),
    path('search/', views.search_bulletin, name='search-bulletin'),
]
