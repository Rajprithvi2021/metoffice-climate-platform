from django.urls import path
from .ui_views import dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
]
