from django.shortcuts import render

from requests.exceptions import RequestException
from weatherGetter.weatherAPI import get_coordinates, get_weather


def index(request):
    return render(request, 'index.html')


def get_city_weather(request):
    city_name = request.GET.get('city_name')
    city_history = request.session.get('city_history', [])
    coord = get_coordinates(city_name)
    if city_name and coord:
        try:
            weather_status = get_weather(coord)
        except RequestException:
            return render(request, '404city.html',
                          context={'name':city_name,
                                   'city_history': city_history})
        if city_name not in city_history:
            if len(city_history) == 10:
                city_history = city_history[1:]
            city_history.append(city_name)
            request.session['city_history'] = city_history
        return render(request, 'weather_table.html', context={'name':city_name,
                                                      'weather_status': weather_status,
                                                      'coord' : coord,
                                                      'city_history': city_history})

    return render(request, '404city.html', context={'name':city_name,
                                                    'city_history': city_history})
    