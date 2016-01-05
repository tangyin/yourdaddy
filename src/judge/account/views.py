# coding=utf8
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import views
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages


from forms import RegistrationForm,LoginForm


def my_user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if User.objects.get(username = ):
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password2'],
                email=form.cleaned_data['email'],
                )
            user.save()
            #注册成功
            name = request.POST["name"]
            return HttpResponseRedirect("/judgesys/index")
    else:
        form = RegistrationForm()
    return render(request,'account/register.html', {'form': form, })


def my_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if not user:
                messages.error(request,u"用户密码错误")
                return render(request, "account/login.html", {"form": form})
            if not user.is_active:
                messages.error(request, u"用户已被禁用，请联系管理员")
                return render(request, "account/login.html", {"form":form})
            login(request, user)
            if request.GET.get("name"):
                return HttpResponseRedirect(request.GET.get("name"))
            return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def my_logout(request):
    logout(request)
    if request.GET.get("name"):
        return HttpResponseRedirect(request.GET.get("name"))
    return HttpResponseRedirect("/")