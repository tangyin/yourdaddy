
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
    if request.method == "POST":
        form = CarJudgeForm(request.POST)
        if form.is_valid():
            car_judge = form.save(commit=False)
            judge_price = car_judge.judge_price()
            return render(request, "judgesys/judge.html",{"form": form, "price":judge_price})
    elif request.method == "GET":
        form = CarJudgeForm()
        return render(request, "judgesys/judge.html", {"form": form})