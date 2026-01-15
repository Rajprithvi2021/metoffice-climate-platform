from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class MetricList(APIView):
    def get(self, req):
        return Response(list(WeatherMetric.objects.values()))

class MonthlyAPI(APIView):
    def get(self, req):
        m = req.GET["metric_id"]
        y = req.GET["year"]
        qs = MonthlyWeatherFact.objects.filter(metric_id=m, year=y)
        return Response({
            "year": y,
            "data": [{"month": q.month, "value": q.value} for q in qs]
        })

class AnnualAPI(APIView):
    def get(self, req):
        m = req.GET["metric_id"]
        qs = AnnualWeatherFact.objects.filter(metric_id=m)
        return Response([{"year": q.year, "value": q.value} for q in qs])
