from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class extendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pict = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name="")

def create_extend(sender, instance, created, **kwargs):
    if created:
        user_extend = extendUser(user=instance)
        user_extend.save()

post_save.connect(create_extend, sender=User)