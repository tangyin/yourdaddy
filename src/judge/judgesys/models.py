# -*- coding:utf-8 -*-
from __future__ import unicode_literals


from django.db import models

# Create your models here.


class CarJudge(models.Model):
    series = models.ForeignKey(CarSeries)
    purchase_date = models.DateField(verbose_name="购买日期")
    sell_out_date = models.DateField(verbose_name="出售日期")
    brand = models.CharField(max_length = 200)
    model = models.CharField(max_length = 200)
    series
