from django.contrib import admin
from .models import Categories, Products, Cart

# Register your models here.


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "price",
        "label",
        "category",
        "image",
        "slug",
        "in_cart",
    ]
    list_display = ["name", "category", "label", "in_cart", "update_at", "created_at"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name", "update_at", "created_at"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields = ["product", "quantity"]
    list_display = ["id", "product", "quantity", "update_at", "created_at"]
