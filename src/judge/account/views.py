# coding=utf8
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import views
from forms import RegistrationForm,LoginForm
from django.shortcuts import render
from django.template import RequestContext


def my_user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password2'],
                email=form.cleaned_data['email'],
                )
            user.save()
            #注册成功
            name = request.POST["name"]
            return HttpResponseRedirect(name)
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
            login(request,user)
            #注册成功
            name = request.POST["name"]
            return HttpResponseRedirect(name)
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form': form }, context_instance=RequestContext(request))


def my_logout(request):
    template_response = views.logout(request,template_name= "account/logout")
    return template_response