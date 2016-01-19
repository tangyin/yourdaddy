# -*- coding:utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"品牌")
    name_initial = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"品牌首字母")

    def __unicode__(self):
        return u"%s" % self.name


class CarSeries(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"系列")
    brand = models.ForeignKey(CarBrand)
    year_to_market = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"上市年份")
    trim = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"型号配置")

    car_category = models.CharField(max_length=2, null=True, blank=True, verbose_name=u'车辆分类')
    seats_num = models.CharField(max_length=2, null=True, blank=True, verbose_name=u'座位数')
    engine = models.CharField(max_length=2, null=True, blank=True, verbose_name=u'驱动方式')
    fuel = models.CharField(max_length=2, null=True, blank=True, verbose_name=u'燃油类型')
    transmission = models.CharField(max_length=30, null=True, blank=True, verbose_name=u'变速器')
    air_displacement = models.CharField(max_length=30, null=True, blank=True,verbose_name=u'排气量')
    air_displacement_unit = models.CharField(max_length=30, null=True, blank=True, verbose_name=u'单位')

    def __unicode__(self):
        return u"%s" % self.name


class CarJudge(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"系列")
    series = models.ForeignKey(CarSeries)
    purchase_year = models.CharField(max_length=20, default="2010", null=True, blank=True, verbose_name=u"购入年份")
    purchase_month = models.CharField(max_length=20, default="1", null=True, blank=True, verbose_name=u"购入年份")
    mileage = models.IntegerField(default=1, null=True, blank=True, verbose_name=u"行驶里程")
    judge_date = models.DateField(auto_now=True, verbose_name= u"评估日期")
    judge_user = models.ForeignKey(User)

    def __unicode__(self):
        return u"%s" % self.name










