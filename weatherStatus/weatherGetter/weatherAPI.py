from geopy.geocoders import Nominatim

import requests

from .constants import WEATHER_CODES


geolocator = Nominatim(user_agent="DjangoWeather")


def get_coordinates(city_name: str):
    location = geolocator.geocode(city_name)
    if location:
        return (location.latitude, location.longitude)
    return None

def get_weather(coord: tuple, timezone: str = 'auto'):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={coord[0]}&longitude={coord[1]}&timezone={timezone}&hourly=temperature_2m,weather_code&forecast_days=1'
    responce = requests.get(url).json().get('hourly')
    time = responce.get('time')
    temp = responce.get('temperature_2m')
    weather = [WEATHER_CODES[code] for code in responce.get('weather_code')]
    context = dict(zip(time, list(zip(temp, weather))))
    return context

