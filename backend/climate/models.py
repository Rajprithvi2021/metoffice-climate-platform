from django.db import models

# Create your models here.
from django.db import models

class WeatherMetric(models.Model):
    parameter = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    source = models.CharField(max_length=100, default="MetOffice")
    unit = models.CharField(max_length=20, default="°C")

    class Meta:
        unique_together = ("parameter", "region")

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
