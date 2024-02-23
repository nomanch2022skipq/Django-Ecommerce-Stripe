from django.contrib import admin
from .models import UserModel

# Register your models here.


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    fields = ["username", "password"]
