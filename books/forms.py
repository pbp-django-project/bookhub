from django import forms
from . import models

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search book'}))

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = models.UserBook
        fields = ["title", "authors", "publisher", "pub_year", "isbn", "cover_img"]
    
    def clean_cover_img(self):
        cover_img = self.cleaned_data.get('cover_img', None)
        if not cover_img:
            # If cover_img is not provided, use the default value
            return 'https://static.thenounproject.com/png/3674271-200.png'
        return cover_img