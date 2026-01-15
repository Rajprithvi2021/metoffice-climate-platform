from django.shortcuts import render

def dashboard(request):
    return render(request, "climate/dashboard.html")
