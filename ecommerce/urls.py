"""ecommerce_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from .views import (
    HomeView,
    BuyProduct,
    addtocart,
    CartPage,
    RemoveItem,
    Shop,
    removefromcart,
    Checkout,
    Payment,
    HandlePayment,
)

urlpatterns = [
    path("", HomeView.as_view(), name="register_view"),
    path("buy/<slug:slug>/", BuyProduct.as_view(), name="single"),
    path("cart/<int:product_id>", addtocart.as_view(), name="addtocart"),
    path("shopping-cart/", CartPage, name="cart"),
    path("removeitem/<int:product_id>/", RemoveItem.as_view(), name="removeitem"),
    path("shop/", Shop.as_view(), name="shop"),
    path(
        "removefromcart/<int:product_id>/",
        removefromcart.as_view(),
        name="removefromcart",
    ),
    path("checkout/", Checkout.as_view(), name="checkout"),
    path("payment/", Payment.as_view(), name="payment"),
    path("handle-payment/", HandlePayment),
]
