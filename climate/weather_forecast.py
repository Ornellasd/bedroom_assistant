import pyowm


owm = pyowm.OWM('96bae3ab3550d3c6c1bde626c2a458e4')
city_id = 5746545

def get_forecast():
    obs = owm.weather_at_id(city_id)
    w = obs.get_weather()
    get_temp = w.get_temperature('fahrenheit')['temp']
    outside_temp = str(get_temp)[:2] + "°F"
    status = w.get_detailed_status().title()
    icon = w.get_weather_icon_name()
    icon_url = 'http://openweathermap.org/img/w/' + icon + '.png'
    derp = [outside_temp, status, icon_url]

    return derp