from django import forms
from . import models

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search book'}))

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = models.UserBook
        fields = ["title", "authors", "publisher", "pub_year", "isbn", "cover_img"]