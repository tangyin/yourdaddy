from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import views
from django.shortcuts import render


def my_user_register(request):
    return render(request, template_name= "account/register.html")


def user_register(request):
    username = request.POST["username"]
    password = request.POST["password"]
    u = User.objects.create_user(username=username,password=password)
    u.save()
    return HttpResponse("CONGRATULATIONS")


def my_login(request):
    template_response = views.login(request, template_name= "account/login.html")
    return template_response


def my_logout(request):
    template_response = views.logout(request,template_name= "account/logout")
    return template_response


def my_password_reset(request):
    pass
