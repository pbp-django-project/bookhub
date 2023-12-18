from django.urls import path
from . import views

app_name = "bulletin"

urlpatterns = [
    path("", views.show_bulletin, name="show-bulletin"),
    path("add-bulletin/", views.add_news_page, name="add-news-page"),
    path("full-news/<int:bulletin_id>", views.show_full_news, name="full-news"),
    path('search/', views.search_bulletin, name='search-bulletin'),
    path('json/', views.show_json, name='show-json' ),
    path('json/<int:id>/', views.show_json_by_id, name="show-json-by-id"),
    path('create-flutter/', views.create_product_flutter, name = "create-product-flutter "),
    path('book-recomendation/', views.show_book_recomendation, name = "show-book-recomendation"),
]
