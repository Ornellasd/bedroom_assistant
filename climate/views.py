from django.shortcuts import render

from . import weather_forecast
from .weather_forecast import *


def index(request):
    """The home page for bedroom-assistant"""
    outside_temp = get_forecast()[0]
    status = get_forecast()[1]    
    icon_url = get_forecast()[2] 
           
    return render(request, 'climate/index.html', {'outside_temp': outside_temp, 'status': status, 'icon_url': icon_url})

