from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models
from . import forms

def get_books(request):
    data = models.Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



def show_books(request):
    books = models.Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "bookpage.html", context)

def search_books(request):
    search = forms.SearchForm(request.GET)
    books = []
    if search.is_valid():
        search_term = search.cleaned_data['q']
        #filter_type = request.GET.get("filter")
        books = models.Book.objects.filter(title__contains = search_term) | models.Book.objects.filter(authors__contains = search_term) | \
                models.Book.objects.filter(publisher__contains = search_term) | models.Book.objects.filter(pub_year__contains = search_term)
                   
    context = {
        'books': books,
        'search': search,
    }
    return render(request, "bookpage.html", context)

@login_required(login_url='main:login')
def add_books(request):
    form = forms.BookUploadForm(request.POST, request.FILES)
    
    if form.is_valid() and request.method == "POST":
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return HttpResponseRedirect(reverse('books:show-books'))

    context = {
        'form': form,
    }
    return render(request, "add_book.html", context)