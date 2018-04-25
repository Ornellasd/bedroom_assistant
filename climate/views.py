from django.shortcuts import render
from django.http import HttpResponseRedirect

from .scripts import weather_forecast, wemo
from .scripts.weather_forecast import *
from .scripts.wemo import *


def index(request):
    """The home page for bedroom-assistant"""
    outside_temp = get_forecast()[0]
    status = get_forecast()[1]    
    icon_url = get_forecast()[2] 
    wemo_state = get_status()

    context = {
        'outside_temp': outside_temp, 
        'status': status,
        'icon_url': icon_url,
        'wemo_state':wemo_state    
    }
    
    return render(request, 'climate/index.html', context)

def desk_on(request):
    on = wemo_on()
    return HttpResponseRedirect('/')
    
def desk_off(request):
    off = wemo_off()
    return HttpResponseRedirect('/')
    