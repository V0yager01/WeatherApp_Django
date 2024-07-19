from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from .constants import CITIES, WRONG_CITY


class TestLogic(TestCase):
    def SetUp(self):
        self.user_client = Client()


    def test_city_history(self):
        for city in CITIES:
            with self.subTest():
                url = reverse('weather:get_weather') + f'?city_name={city}'
                response = self.client.get(url)
                self.assertIn(city, response.context['city_history'])
        self.assertNotEqual(len(response.context['city_history']), 11)
    
    
    def test_invalid_city_name(self):
        url = reverse('weather:get_weather') + f'?city_name={WRONG_CITY}'
        response = self.client.get(url)
        self.assertTemplateUsed(response, '404city.html')

