import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from itertools import chain
from . import models
from . import forms
from django.contrib.auth.models import User


def show_books(request):
    books = models.Book.objects.all()
    user_books = models.UserBook.objects.all()
    data = list(chain(books, user_books))
    context = {
        'books': data
    }
    return render(request, "bookpage.html", context)


def show_json_b_by_id(request, id):
    books = models.Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", books), content_type="application/json")

def show_json_ub_by_id(request, id):
    books = models.UserBook.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", books), content_type="application/json")

def search_books(request):
    search = forms.SearchForm(request.GET)
    search_filter = request.GET.get('filter', 'all')
    
    if search.is_valid():
        search_term = search.cleaned_data['q']
        data = []

        if search_filter == 'all':
            books = models.Book.objects.filter(title__contains = search_term) | models.Book.objects.filter(authors__contains = search_term) | \
                    models.Book.objects.filter(publisher__contains = search_term)
            user_books = models.UserBook.objects.filter(title__contains = search_term) | models.UserBook.objects.filter(authors__contains = search_term) | \
                        models.UserBook.objects.filter(publisher__contains = search_term)
            data = list(chain(books, user_books))

        elif search_filter == 'title':
            books = models.Book.objects.filter(title__contains = search_term)
            user_books = models.UserBook.objects.filter(title__contains = search_term)
            data = list(chain(books, user_books))

        elif search_filter == 'author':
            books = models.Book.objects.filter(authors__contains = search_term)
            user_books = models.UserBook.objects.filter(authors__contains = search_term)
            data = list(chain(books, user_books))

        elif search_filter == 'publisher':
            books = models.Book.objects.filter(publisher__contains = search_term)
            user_books =  models.UserBook.objects.filter(publisher__contains = search_term)
            data = list(chain(books, user_books))

    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

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

def get_books(request):
    data = models.Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_userbooks(request):
    data = models.UserBook.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def add_books_mobile(request):
    if request.method == 'POST':

        user = User.objects.get(username=request.user.username)
        data = json.loads(request.body)
        print(user)
      
        add_books = models.UserBook.objects.create(
            user = user,
            title = data["title"],
            authors = data["authors"],
            publisher = data["publisher"],
            pub_year = int(data["pub_year"]),
            isbn = data["isbn"],
            cover_img = data["cover_img"]
        )

        add_books.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)