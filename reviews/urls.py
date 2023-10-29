from django.urls import path
from reviews.views import show_reviews, get_review_json, add_review_ajax, show_json, create_review, details_review, remove_ajax, edit_review

app_name = 'reviews'

urlpatterns = [
    path('reviews/<int:book_id>/', show_reviews, name='show_reviews'),
    path('get-review/<int:book_id>/', get_review_json, name='get_review_json'),
    path('add-review/<int:book_id>/', add_review_ajax, name='add_review_ajax'),
    path('create-review/<int:book_id>/', create_review, name='create_review'),
    path('details-review/<int:review_id>/', details_review, name='details_review'),
    path('show-json/', show_json, name='show_json'),
    path('remove-ajax/', remove_ajax, name='remove_ajax'),
    path('edit-review/', edit_review, name='edit_review'),
]