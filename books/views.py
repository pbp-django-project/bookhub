from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from . import models

def get_books(request):
    data = models.Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



def show_books(request):
    books = models.Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "bookpage.html", context)