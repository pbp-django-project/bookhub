from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    # Untuk mengatur metadata pada web admin
    class Meta:
        ordering = ('name',) #order berdasarkan lexico nama
        verbose_name_plural = 'Genres' #mengganti nama plural
    
    # Untuk menampilkan objek apa saja yang sudah kita buat untuk models Genre
    def __str__(self):
        return self.name
    
class Book(models.Model):
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Untuk mengatur metadata pada web admin
    class Meta:
        ordering = ('name',) #order berdasarkan lexico nama
        verbose_name_plural = 'Books' #mengganti nama plural