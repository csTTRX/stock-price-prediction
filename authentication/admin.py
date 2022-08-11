import email
import imp
from django.contrib import admin
from .models import User


class User_admin(admin.ModelAdmin):
    list_display=['email','is_active','username'

    ]



admin.site.register(User,User_admin)
