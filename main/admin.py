from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

admin.site.unregister(Group)

class UserInline(admin.StackedInline):
    model = extendUser

class UserAdmin(admin.ModelAdmin):
    model= User
    fields = ["username", "email"]
    inlines = [UserInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)