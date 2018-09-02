from django.contrib import admin
from customuser.models import CustomUser

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


admin.site.register(CustomUser, UserAdmin)

