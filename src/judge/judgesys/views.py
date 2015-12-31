from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated():
        username = request.user
    else:
        username = ""
    return render(request,"judgesys/index.html",{"username":username})