# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class CarBrand(models.Model):
    """
    车辆品牌 example：bmw
    """
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="车辆品牌" )

    def __unicode__(self):
        return u'%s' % self.name


class CarModel(models.Model):
    """
    车型 example：奥迪A4L
    """
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="车型" )
    car_brand = models.ForeignKey(CarBrand)

    def __unicode__(self):
        return u'%s' % self.name


class CarSeries(models.Model):
    """
    车系 example：奥迪A4L 2016款 30 TFSI 自动舒适型
    """
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="车系" )
    car_brand = models.ForeignKey(CarModel)
    official_price = models.IntegerField(default=0, verbose_name= "官方指导价")
    color = models.CharField(max_length=100, null=True, blank=True, verbose_name="颜色" )

    def __unicode__(self):
        return u'%s' % self.name


class CarDatabase(models.Model):
    """
    已经有成交价的二手车数据库
    """
    series = models.ForeignKey(CarSeries)
    purchase_date = models.DateField(auto_now_add=True, verbose_name="购买日期")
    sell_out_date = models.DateField(auto_now_add=True, verbose_name="出售日期")
    price = models.IntegerField(default=0, verbose_name="二手成交价")