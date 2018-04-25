from django.shortcuts import render

from . import weather_forecast, wemo
from .weather_forecast import *
from .wemo import *


def index(request):
    """The home page for bedroom-assistant"""
    outside_temp = get_forecast()[0]
    status = get_forecast()[1]    
    icon_url = get_forecast()[2] 
    wemo_state = get_status()

    return render(request, 'climate/index.html', {'outside_temp': outside_temp, 'status': status, 'icon_url': icon_url, 'wemo_state':wemo_state})

def desk_on(request):
    on = wemo_on()
    wemo_state = get_status()
    outside_temp = get_forecast()[0]
    status = get_forecast()[1]    
    icon_url = get_forecast()[2] 
       
    return render(request, 'climate/index.html', {'on': on, 'wemo_state': wemo_state, 'outside_temp': outside_temp, 'status': status, 'icon_url': icon_url})

def desk_off(request):
    off = wemo_off()
    wemo_state = get_status()
    outside_temp = get_forecast()[0]
    status = get_forecast()[1]    
    icon_url = get_forecast()[2] 
       
    return render(request, 'climate/index.html', {'off': off, 'wemo_state': wemo_state, 'outside_temp': outside_temp, 'status': status, 'icon_url': icon_url})