from typing import Any
from django.http import HttpRequest
from django.shortcuts import (
    HttpResponse as HttpResponse,
    render,
    HttpResponse,
    redirect,
)
from django.views.generic import TemplateView, View
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password

# from django
from .models import UserModel

# Create your views here.


class UserLoginView(TemplateView):
    template_name = "login.html"

    def post(self, request):
        data = request.POST
        username = data["username"]
        password = data["password"]

        auth = authenticate(request, username=username, password=password)
        if auth:
            return redirect("/home/")

        else:
            return HttpResponse("Please Enter Valid Username and Password")


class UserRegisterView(TemplateView):
    template_name = "register.html"

    def post(self, request):
        data = request.POST

        username = data["username"]
        password = data["password"]

        register = UserModel.objects.create(
            username=username, password=make_password(password)
        )
        if register:
            return redirect("/accounts/login/")



