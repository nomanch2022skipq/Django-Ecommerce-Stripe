from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import Categories, Products, Cart, Order

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


from django.contrib import admin
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.html import format_html

from .models import Order


from django.contrib import messages


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ["charge_id"]
    list_display = ["charge_id", "update_at", "created_at"]
    readonly_fields = ["charge_id", "update_at", "created_at"]

    def delete_view(self, request, object_id, extra_context=None):
        messages.error(request, "This order cannot be deleted")
        return HttpResponseRedirect(reverse("admin:ecommerce_order_changelist"))
