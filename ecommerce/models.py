from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Categories(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Products(BaseModel):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="products")
    price = models.IntegerField()
    label = models.CharField(max_length=100, null=True, blank=True)
    in_cart = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Carddata(BaseModel):
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.card_number


class Cart(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Order(BaseModel):
    charge_id = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def delete(self, *args, **kwargs):
        raise ValidationError("This field cannot be deleted.")
