# -*- coding:utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.
transmission_choice = (
    ('A', u'手动'),
    ('B', u'自动'),
)

brand_choice = (
    ('A', u'宝马'),
    ('B', u'奔驰'),
)


class CarBrand(models.Model):
    name = models.CharField(choices=brand_choice, max_length=100, null=True, blank=True, verbose_name=u"品牌")
    name_initial = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"品牌首字母")

    def __unicode__(self):
        return u"%s" % self.name


class CarSeries(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"系列")
    brand = models.ForeignKey(CarBrand,verbose_name= u"品牌")
    year_to_market = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"上市年份")
    trims = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"内饰配置")
    market_price = models.IntegerField(default=10, null=True, blank=True, verbose_name=u"官方推荐价")

    transmission = models.CharField(choices=transmission_choice, max_length=30, null=True, blank=True, verbose_name=u'变速器')

    def __unicode__(self):
        return u"%s%s" % (self.name,self.trims)


class CarJudge(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"系列")
    series = models.ForeignKey(CarSeries, verbose_name=u"型号配置")
    purchase_year = models.CharField(max_length=20, default="2010", null=True, blank=True, verbose_name=u"购入年份")
    mileage = models.IntegerField(default=1, null=True, blank=True, verbose_name=u"行驶里程")
    judge_date = models.DateField(auto_now=True, verbose_name= u"评估日期")
    judge_user = models.ForeignKey(User)

    def judge_price(self):
        price = self.series.market_price
        year_now = time.strftime('%Y', time.localtime(time.time()))
        years_used = int(year_now) - (int(self.purchase_year))

        return price *0.8 * (0.9 ** years_used) * (0.98 ** self.mileage)




    def __unicode__(self):
        return u"%s" % self.name










