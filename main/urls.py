from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('signup/', views.signup_user, name = 'signup'),
    path('login/', views.login_user, name='login'),
    
]