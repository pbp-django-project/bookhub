from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import extendUser
from django.forms.widgets import ClearableFileInput

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
class PictForm(forms.ModelForm):
    class Meta:
        model = extendUser
        fields = ('profile_pict', )