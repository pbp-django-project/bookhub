from itertools import chain
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


def show_collection(request): # harusnya tambahin id
    # books = models.Collection.objects.all()
    books = models.Collection.objects.all() # harusnya ganti filter(pk = id)
    user_books = models.UserBook.objects.all()
    data = list(chain(books, user_books))
    context = {
        'books': data
    }
    return render(request, "mybook_page.html", context)

def search_collection(request):
    search = forms.SearchForm(request.GET)
    search_filter = request.GET.get('filter', 'all')

    if search.is_valid():
        search_term = search.cleaned_data['q']
        data = []

        if search_filter == 'all':
            books = models.Collection.objects.filter(title__contains = search_term) | models.Collection.objects.filter(authors__contains = search_term) | \
                    models.Collection.objects.filter(publisher__contains = search_term)
            user_books = models.UserBook.objects.filter(title__contains = search_term) | models.UserBook.objects.filter(authors__contains = search_term) | \
                        models.UserBook.objects.filter(publisher__contains = search_term)
            data = list(chain(books, user_books))

        elif search_filter == 'title':
            books = models.Collection.objects.filter(title__contains = search_term)
            user_books = models.UserBook.objects.filter(title__contains = search_term)
            data = list(chain(books, user_books))

        elif search_filter == 'author':
            books = models.Collection.objects.filter(authors__contains = search_term)
            user_books = models.UserBook.objects.filter(authors__contains = search_term)
            data = list(chain(books, user_books))

        elif search_filter == 'publisher':
            books = models.Collection.objects.filter(publisher__contains = search_term)
            user_books =  models.UserBook.objects.filter(publisher__contains = search_term)
            data = list(chain(books, user_books))

    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@login_required(login_url='main:login')
def add_collection(request):
    form = forms.BookUploadForm(request.POST, request.FILES)
    
    if form.is_valid() and request.method == "POST":
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return HttpResponseRedirect(reverse('collection:show-collection'))

    context = {
        'form': form,
    }
    return render(request, "add_book.html", context)

def get_collection(request):
    data = models.Collection.objects.all()
    # data = models.Collection.objects.filter(pk = id) # ngubah dari punya naufal
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")