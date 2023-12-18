from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import SignUpForm, PictForm
from books.models import Book
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import extendUser


def homepage(request):
    context = {
        'user': request.user,
        'username': request.user.username
    }
    return render(request, 'homepage.html', context)

@csrf_exempt
def signup_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')

    context = {'form':form}
    return render(request, 'signup.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:homepage")) 
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:homepage')

@csrf_exempt
def update_user(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        user_pict = extendUser.objects.get(user__id=request.user.id)
        form = SignUpForm(request.POST or None, instance=user)
        pict_form = PictForm(request.POST or None, instance=user_pict)
        if form.is_valid() and pict_form.is_valid():
            form.save()
            pict_form.save()
            login(request, user)
            return redirect('main:homepage')
        return render(request, 'profile.html', {'form':form, 'user':user, 'pict_form':pict_form,})
    else:
        return redirect('main:homepage')