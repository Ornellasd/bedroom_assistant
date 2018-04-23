from django.shortcuts import render


def index(request):
    """The home page for bedroom-assistant"""
    return render(request, 'climate/index.html')

