# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


car_category_choice = (
    ('A', u'轿车'),
    ('B', u'越野车'),
    ('C', u'跑车'),
    ('D', u'商务车'),
    ('E', u'房车'),
    ('F', u'特种车'),
)

seats_num_choice = {
    ('A', u'五座'),
    ('B', u'七座'),
    ('C', u'双座'),
}

engine_choice = {
    ('A', u'两驱'),
    ('B', u'四驱')
}

fuel_choice = (
    ('A', u'汽油'),
    ('B', u'汽电混合'),
    ('C', u'电动'),
    ('D', u'柴油'),
)

transmission_choice = (
    ('A', u'手自一体'),
    ('B', u'自动'),
    ('C', u'手动'),
    ('D', u'双离合'),
)

air_displacement_unit_choice = (
    ('A', u'L'),
    ('B', u'T'),
)


class CarBrand(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'车辆厂商名称')
    name_initial = models.CharField(max_length=2, null=True, blank=True, verbose_name=u'名称首字母')

    def __unicode__(self):
        return u'%s' % self.name


class CarSeries(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'车辆品牌名称')
    brand = models.ForeignKey(CarBrand)
    series_type = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'类型')

    def __unicode__(self):
        return u'%s' % self.name


class CarModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'车辆型号名称')
    series = models.ForeignKey(CarSeries)
    year_model = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'类型')
    car_category = models.CharField(choices=car_category_choice, max_length=2, null=True, blank=True,
                                    verbose_name=u'车辆分类')
    seats_num = models.CharField(choices=seats_num_choice, max_length=2, null=True, blank=True, verbose_name=u'座位数')
    engine = models.CharField(choices=engine_choice, max_length=2, null=True, blank=True, verbose_name=u'驱动方式')
    fuel = models.CharField(choices=fuel_choice, max_length=2, null=True, blank=True, verbose_name=u'燃油类型')
    transmission = models.CharField(choices=transmission_choice, max_length=30, null=True, blank=True,
                                    verbose_name=u'变速器')
    air_displacement = models.CharField(max_length=30, null=True, blank=True, verbose_name=u'排气量')
    air_displacement_unit = models.CharField(choices=air_displacement_unit_choice, max_length=30, null=True, blank=True,
                                             verbose_name=u'单位')

    def __unicode__(self):
        return u'%s' % self.name