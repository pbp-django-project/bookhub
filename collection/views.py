from itertools import chain
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from . import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def show_collection(request): # harusnya tambahin id
    # books = models.Collection.objects.all()
    # books = Collection.objects.all() # harusnya ganti filter(pk = id)
    user_books = UserBook.objects.all().filter(user = request.user)
    # data = list(chain(books, user_books))
    context = {
        'books': user_books
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

def get_collection(request, id):
    # data = models.Collection.objects.all()
    data = models.UserBook.objects.get(pk = id) # ngubah dari punya naufal
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def delete_collection(request, id):
    # Get data berdasarkan ID
    product = models.UserBook.objects.get(pk = id)
    # Hapus data
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('collection:show-collection'))


def edit_book(request, id):
    book = get_object_or_404(models.UserBook, pk=id)

    if request.method == 'POST':
        form = forms.BookUploadForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('collection:show-collection'))
    else:
        form = forms.BookUploadForm(instance=book)

    context = {
        'form': form,
    }
    return render(request, 'edit_book.html', context)

# def edit_book(request, pk):
#     if request.method == 'POST':
#         book = get_object_or_404(models.Collection, pk=pk)
#         # Perform the edit operation here
#         # You will need to take the data from the request and update the book object
#         # Once the book object is updated, save it to the database
#         book.save()
#         return HttpResponse('Book updated')

# def delete_book(request, pk):
#     if request.method == 'POST':
#         book = get_object_or_404(models.Collection, pk=pk)
#         book.delete()
#         return HttpResponse('Book deleted')

def get_userbooks(request):
    data = models.UserBook.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_collection_mobile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(username=data["username"])

        add_collection = models.UserBook.objects.create(
            user = user,
            title = data["title"],
            authors = data["authors"],
            publisher = data["publisher"],
            pub_year = int(data["pub_year"]),
            isbn = data["isbn"],
            cover_img = data["cover_img"]
        )

        add_collection.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def show_collection_mobile(request):
    data = json.loads(request.body)
    print(data["username"])
    user = User.objects.get(username=data["username"])
        

    books = UserBook.objects.all().filter(user = user)

    return HttpResponse(serializers.serialize("json", books), content_type="application/json")