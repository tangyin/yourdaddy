
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from forms import CarJudgeForm
from models import CarJudge

from django.forms import modelformset_factory


def index(request):
    if request.user.is_authenticated():
        username = request.user
    else:
        username = ""
    return render(request, "judgesys/index.html", {"username": username})


def judge(request):
    JudgeFormSet = modelformset_factory(CarJudge,fields=)
    if request.method == "POST":
        form = CarJudgeForm(request.POST)
        if form.is_valid():


    elif request.method == "GET":
        form = CarJudgeForm()
        render(request, "judgesys/judge.html", {"form": form})


