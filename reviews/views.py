import json
from django.shortcuts import render
from reviews.models import Review
from books.models import Book
from reviews.forms import ReviewForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
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
    return HttpResponse(serializers.serialize('json', reviews), content_type="application/json")

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

@csrf_exempt
def create_review_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Ensure that the user is authenticated before creating the review
            if request.user.is_authenticated:
                user = request.user
            else:
                # If the user is not authenticated, you can handle it accordingly.
                # For example, you might want to return an error response.
                return JsonResponse({"status": "error", "message": "User is not authenticated"}, status=402)

            new_review = Review.objects.create(
                book=Book.objects.get(pk=int(data["book_id"])),
                user=user,
                title=data["title"],
                rating=int(data["rating"]),
                comment=data["comment"],
                username=user.username,
            )

            new_review.save()
            print(request.user.username)
            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            # Log or print the exception for debugging
            print(f"Error creating review: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def edit_review_flutter(request):
    # Check if the user is authenticated
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Ensure that the user is authenticated before editing the review
            if not request.user.is_authenticated:
                return JsonResponse({"status": "error", "message": "User is not authenticated"}, status=402)

            # Get the existing review based on review_id and check if the user owns the review
            review_id = int(data.get("review_id", 0))
            try:
                review = Review.objects.get(pk=review_id, user=request.user)
            except Review.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Review not found or user does not own the review"}, status=404)

            # Update the existing review
            review.book = Book.objects.get(pk=int(data.get("book_id")))
            review.title = data.get("title", "")
            review.rating = int(data.get("rating", 0))
            review.comment = data.get("comment", "")
            review.username = request.user.username
            review.save()

            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            # Log or print the exception for debugging
            print(f"Error updating review: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def delete_review_flutter(request):
    data = json.loads(request.body)
    review_id = int(data.get("review_id", 0))
    review = Review.objects.get(pk=review_id)

    # Check if the user is the owner of the review
    if request.user == review.user:
        review.delete()
        return JsonResponse({"status": "success", "message": "Review deleted successfully"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "User is not authorized to delete this review"}, status=403)
    
@csrf_exempt
def check_username_flutter(request):
    if request.user.is_authenticated:
                user = request.user
    else:
                # If the user is not authenticated, you can handle it accordingly.
                # For example, you might want to return an error response.
        return JsonResponse({"status": "error", "message": "User is not authenticated"}, status=402)
    user_data = {
        'username': user.username,
        'status': 'success'
        # Add any other user-related fields you want to include
    }
    print(f"User Data: {user_data}")
    return JsonResponse(user_data, status=200)

@csrf_exempt
def get_avg_flutter(request):
    if request.user.is_authenticated:
                user = request.user
    else:
                # If the user is not authenticated, you can handle it accordingly.
                # For example, you might want to return an error response.
        return JsonResponse({"status": "error", "message": "User is not authenticated"}, status=402)
    data = json.loads(request.body)
    book_id = int(data.get("book_id", 0))
    try:
        book = Book.objects.get(pk=book_id)
        reviews = Review.objects.filter(book=book)

        if reviews.exists():
            average_rating = sum(review.rating for review in reviews) / reviews.count()
        else:
            average_rating = 0.0

        user_data = {
            'avg': average_rating,
            'status': 'success'
            # Add any other user-related fields you want to include
        }
        print(f"User Data: {user_data}")
        return JsonResponse(user_data, status=200)
    except Book.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Book does not exist"}, status=404)

@csrf_exempt
def has_user_made_review_flutter(request):
    if request.user.is_authenticated:
                user = request.user
    else:
                # If the user is not authenticated, you can handle it accordingly.
                # For example, you might want to return an error response.
        return JsonResponse({"status": "error", "message": "User is not authenticated"}, status=402)
    
    data = json.loads(request.body)
    book_id = int(data.get("book_id", 0))
    try:
        book = Book.objects.get(pk=book_id)
        reviews = Review.objects.filter(book=book, user=user)

        if reviews.exists():
            res = True
        else:
            res = False

        user_data = {
            'hasMadeReview': res,
            'status': 'success'
            # Add any other user-related fields you want to include
        }
        print(f"User Data: {user_data}")
        return JsonResponse(user_data, status=200)
    except Book.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Book does not exist"}, status=404)