from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import Categories, Products, Cart
from django.views import View
from django.db import models


# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        categories = Categories.objects.all()
        products = Products.objects.all()
        return self.render_to_response(
            context={"categories": categories, "products": products}
        )


class BuyProduct(TemplateView):
    template_name = "buyproduct.html"

    def get_context_data(self, slug):
        data = Products.objects.filter(slug=slug)
        return {"context": data}


class addtocart(View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("product_id")

        if Cart.objects.filter(product_id=product_id).exists():
            cart = Cart.objects.get(product_id=product_id)
            cart.quantity += 1
            cart.save()
        else:
            cart = Cart.objects.create(product_id=product_id, quantity=1)
            cart.product.in_cart = True
            cart.product.save()

        if request.is_ajax():
            return JsonResponse({"success": True})
        else:
            return redirect("cart")


class removefromcart(View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("product_id")

        try:
            cart_item = Cart.objects.get(product_id=product_id)
            product = Products.objects.get(name=cart_item.product.name)
            product.in_cart = False
            product.save()
            cart_item.delete()
            return JsonResponse({"success": True})
        except Cart.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Item not found in the cart"}
            )


def CartPage(request, *args, **kwargs):
    print(request.method)
    cart_items = Cart.objects.all()
    total_price_of_cart_item = Cart.objects.aggregate(models.Sum("product__price"))
    context = {
        "cart_items": cart_items,
        "totat_price": total_price_of_cart_item,
        "length_of_items": len(cart_items),
    }
    return render(request, "shopping-cart.html", context)


class RemoveItem(View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("product_id")
        print(product_id)
        remove_item = Cart.objects.get(id=product_id)
        product = Products.objects.get(name=remove_item.product.name)
        product.in_cart = False
        product.save()
        remove_item.delete()

        return redirect("cart")


class Shop(TemplateView):
    template_name = "shop.html"

    def get(self, request):
        categories = Categories.objects.all()
        products = Products.objects.all()
        return self.render_to_response(
            context={"categories": categories, "products": products}
        )


class Checkout(TemplateView):
    template_name = "checkout.html"

    def get(self, request):
        total_price_of_cart_item = Cart.objects.aggregate(models.Sum("product__price"))
        cart_items = Products.objects.filter(in_cart=True)
        context = {
            "total_price_of_cart_item": total_price_of_cart_item,
            "cart_items": cart_items,
        }

        return self.render_to_response(context)
