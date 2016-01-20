from django.contrib import admin

# Register your models here.
from .models import CarJudge,CarBrand,CarSeries


admin.site.register(CarJudge)
admin.site.register(CarBrand)
admin.site.register(CarSeries)
