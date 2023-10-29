from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import extendUser
from django.forms.widgets import ClearableFileInput

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        error_messages={'required': 'Please provide a username.'}
    )
    password1 = forms.CharField(
        error_messages={'required': 'A password is required.'}
    )
    password2 = forms.CharField(
        error_messages={'required': 'Please confirm the password.'}
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
class PictForm(forms.ModelForm):
    class Meta:
        model = extendUser
        fields = ('profile_pict', )