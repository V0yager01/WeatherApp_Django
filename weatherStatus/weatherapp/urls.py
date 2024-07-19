from django.urls import path

from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.get_city_weather, name='get_weather')
]