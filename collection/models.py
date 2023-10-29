from django.db import models
from books.models import UserBook

# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    authors = models.CharField(max_length=255, null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    pub_year = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=255, null=True, blank=True)
    cover_img = models.URLField(null=True, blank=True)  

    def __str__(self):
        return self.title
    # Untuk mengatur metadata pada web admin
    class Meta:
        ordering = ('title',) #order berdasarkan lexico nama
        verbose_name_plural = 'Books' #mengganti nama plural