from main.models import extendUser
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

userr = None
@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            userr = user
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "pict": extendUser.objects.get(user=user).profile_pict,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        userr = None
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Registration successful!"
            }, status=200)
        except:
            return JsonResponse({
                "status": False,
                "message": "Registration failed."
            }, status=401)
    else:
        return JsonResponse({
                "status": False,
                "message": "Invalid request method."
            }, status=401)

@csrf_exempt
def update_user_flutter(request):
    if request.method == 'POST':
        pict = request.POST.get('pict')
        print(pict)

        if (pict != ""):
            user = User.objects.get(username=request.user.username)
            extendUser.objects.filter(user=user).update(profile_pict=pict)
            return JsonResponse({
                "status": True,
                "message": "Update successful!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Update failed."
            }, status=401)
    else:
        return JsonResponse({
                "status": False,
                "message": "Invalid request method."
            }, status=401)