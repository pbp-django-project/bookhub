from django.shortcuts import render
from reviews.models import Review
from books.models import Book
from reviews.forms import ReviewForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

# Create your views here.
@login_required(login_url='main:login')
def show_reviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = Review.objects.filter(book=book)
    review_user = Review.objects.filter(book=book, user=request.user)
    average_rating = Review.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']
    context = {
        'reviews': reviews,
        'book' : book,
        'book_id' : book_id,
        'user': request.user,
        'username' : request.user.username,
        'users' : User.objects.all(),
        'average_rating' : average_rating,
        'review_user' : review_user
    }
    return render(request, "reviews.html", context)

def show_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_review_json(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', reviews))

# @csrf_exempt
def create_review(request, book_id):
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.instance.book_id = book_id 
        form.instance.user = request.user
        form.save()
        # review = form.save(commit=False)
        # review.user = request.user
        # review.save()
        return HttpResponseRedirect(reverse('reviews:show_reviews', args=[book_id]))

    context = {'form': form, 'user' : request.user}
    return render(request, "create_review.html", context)

def details_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    context = {
        'review': review,
        'user' : request.user
    }
    return render(request, "review_details_discussion.html", context)

@csrf_exempt
def add_review_ajax(request, book_id):
    if request.method == 'POST':
        title = request.POST.get("title")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        book = Book.objects.get(pk=book_id)

        new_review = Review(title=title, rating=rating, comment=comment, book=book)
        new_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def remove_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        data = Review.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

def edit_review(request, review_id, book_id):
    # Get product berdasarkan ID
    review = Review.objects.get(pk = review_id)

    # Set product sebagai instance dari form
    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('reviews:show_reviews', args=[book_id]))

    context = {'form': form}
    return render(request, "edit_review.html", context)