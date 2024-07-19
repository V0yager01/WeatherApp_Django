from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse


class TestRoutes(TestCase):
    def SetUp(self):
        self.user_client = Client()


    def test_index_page(self):
        url = reverse('weather:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    

    def test_weather_page(self):
        url = reverse('weather:get_weather')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)