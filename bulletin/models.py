from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bulletin(models.Model):
    title = models.CharField(max_length=200,unique=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField()
    # Tambahkan bidang lain yang Anda perlukan

