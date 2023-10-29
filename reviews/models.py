from django.db import models
from books.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    username = models.CharField(max_length=100)