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

from forms import RegistrationForm,LoginForm


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
            return HttpResponseRedirect("/index")
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
            response = HttpResponseRedirect(name)
            return response
    elif request.user.is_authenticated():
        return HttpResponseRedirect("/judgesys/index")
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form': form }, context_instance=RequestContext(request))

@login_required
def my_logout(request):
    logout(request)
    response = HttpResponseRedirect("/judgesys/index")
    return response