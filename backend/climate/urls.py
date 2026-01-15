from django.urls import path
from .views import *

urlpatterns = [
    path("metrics/", MetricList.as_view()),
    path("weather/monthly/", MonthlyAPI.as_view()),
    path("weather/annual/", AnnualAPI.as_view()),
]
