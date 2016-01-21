# -*- coding:utf-8 -*-

from django import forms
from .models import CarJudge

# Create the form class.


class CarJudgeForm(forms.Form):
    brand = forms.CharField(max_length=100,label=u"选择品牌", widget=forms.widgets.Select())
    series = forms.CharField(max_length=100,label=u"选择型号", widget=forms.widgets.Select())
    purchase_year = forms.IntegerField(label=u"购买时间")
    mileage = forms.IntegerField(label=u"行驶里程")


