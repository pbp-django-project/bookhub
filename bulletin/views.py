from django.shortcuts import render
from django.db.models import Q
from .models import Bulletin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from bulletin.forms import BulletinForm

from books.models import Book

# Create your views here.


def show_bulletin(request):
    bulletins = Bulletin.objects.all()
    return render(request, "bulletin_page.html", {"bulletins": bulletins})


def add_news_page(request):
    form = BulletinForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        print("bisa ga ya?")
        form.save()
        return HttpResponseRedirect(reverse("bulletin:show-bulletin"))
    else:
        print(form.errors)

    context = {"form": form}
    return render(request, "add_news_page.html", context)


def show_full_news(request, bulletin_id):
    news = Bulletin.objects.get(pk=bulletin_id)
    return render(request, "full_news.html", {"news": news})

def search_bulletin(request):
    query = request.GET.get("q")  # Mengambil query pencarian dari parameter GET 'q'
    if query:
        bulletins = Bulletin.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        bulletins = Bulletin.objects.all()

    return render(request, "search_results.html", {"bulletins": bulletins, "query": query})

def recomendation_bulletin(request):
    latest_books = Book.objects.all().order_by('pub_year')
    for book in latest_books:
        print(book.title, book.pub_year)


    return render(request, 'bulletin_page.html', {'latest_books': latest_books})