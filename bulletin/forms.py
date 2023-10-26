from django.forms import ModelForm
from bulletin.models import Bulletin
class BulletinForm(ModelForm):
    class Meta:
        model = Bulletin
        fields = ["title", "author", "date_published","content"]