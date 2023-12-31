import json
from django.shortcuts import render
from django.db.models import Q
from .models import Bulletin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from bulletin.forms import BulletinForm
from books.models import Book
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='main:login')
def show_bulletin(request):
    bulletins = Bulletin.objects.all().order_by('title')
    latest_books = Book.objects.all().order_by("-pub_year")[:5]
    paginator = Paginator(bulletins, 5)  # Menggunakan 5 berita per halaman
    page = request.GET.get("page")
    bulletins = paginator.get_page(
        page
    )  # Menggunakan halaman yang dipilih oleh pengguna

    return render(
        request,
        "bulletin_page.html",
        {"bulletins": bulletins, "latest_books": latest_books},
    )


def add_news_page(request):
    form = BulletinForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
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
    bulletins = Bulletin.objects.all().order_by('title')
    latest_books = Book.objects.all().order_by("-pub_year")[:5]

    if query:
        bulletins = bulletins.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    paginator = Paginator(bulletins, 5)  # Menggunakan 5 berita per halaman
    page = request.GET.get("page")
    bulletins = paginator.get_page(
        page
    )  # Menggunakan halaman yang dipilih oleh pengguna

    return render(
        request,
        "bulletin_page.html",
        {"query": query, "bulletins": bulletins, "latest_books": latest_books},
    )

def show_json(request):
    data = Bulletin.objects.all()
    serialized_data = serializers.serialize("json", data)
    return HttpResponse(serialized_data, content_type="application/json")

def show_json_by_id(request, id):
    data = Bulletin.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json",data), content_type= "application/json")

def show_book_recomendation(request):
    data = Book.objects.all().order_by("-pub_year")[:5]
    return HttpResponse(serializers.serialize("json",data), content_type= "application/json")


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_product = Bulletin.objects.create(
            title = data["title"],
            content = data["content"],
            author = data["author"],
            date_published = data["date_published"],

        )
        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

