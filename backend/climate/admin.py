from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(WeatherMetric)
admin.site.register(MonthlyWeatherFact)
admin.site.register(SeasonalWeatherFact)
admin.site.register(AnnualWeatherFact)
