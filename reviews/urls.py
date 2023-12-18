from django.urls import path
from reviews.views import show_reviews, get_review_json, add_review_ajax, show_json, create_review, details_review, remove_ajax, edit_review
from reviews.views import create_review_flutter, edit_review_flutter, check_username_flutter, delete_review_flutter

app_name = 'reviews'

urlpatterns = [
    path('reviews/<int:book_id>/', show_reviews, name='show_reviews'),
    path('get-review/<int:book_id>/', get_review_json, name='get_review_json'),
    path('add-review/<int:book_id>/', add_review_ajax, name='add_review_ajax'),
    path('create-review/<int:book_id>/', create_review, name='create_review'),
    path('details-review/<int:review_id>/', details_review, name='details_review'),
    path('show-json/', show_json, name='show_json'),
    path('remove-ajax/', remove_ajax, name='remove_ajax'),
    path('edit-review/<review_id>/<book_id>/', edit_review, name='edit_review'),
    path('create-review-flutter/', create_review_flutter, name='create_review_flutter'),
    path('edit-review-flutter/', edit_review_flutter, name='edit_review_flutter'),
    path('check-username-flutter/', check_username_flutter, name='check_username_flutter'),
    path('delete-review-flutter/', delete_review_flutter, name='delete_review_flutter'),
]