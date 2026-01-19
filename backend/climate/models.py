from django.db import models

# Create your models here.
from django.db import models

class Region(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)


class Parameter(models.Model):
    code = models.CharField(max_length=20, unique=True)
    unit = models.CharField(max_length=20)

class WeatherMetric(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    source = models.CharField(max_length=100, default="MetOffice")

    class Meta:
        unique_together = ("region", "parameter")


class MonthlyWeatherFact(models.Model):
    metric = models.ForeignKey(WeatherMetric, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    value = models.FloatField(null=True)

    class Meta:
        unique_together = ("metric", "year", "month")

class SeasonalWeatherFact(models.Model):
    metric = models.ForeignKey(WeatherMetric, on_delete=models.CASCADE)
    year = models.IntegerField()
    season = models.CharField(max_length=10)
    value = models.FloatField(null=True)

class AnnualWeatherFact(models.Model):
    metric = models.ForeignKey(WeatherMetric, on_delete=models.CASCADE)
    year = models.IntegerField()
    value = models.FloatField(null=True)
