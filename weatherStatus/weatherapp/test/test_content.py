from django.test import Client, TestCase
from django.urls import reverse

from .constants import (CITIES,
                        PAGE_CONTENT,
                        PAGE404_CONTENT,
                        WRONG_CITY)


class TestContent(TestCase):
    def SetUp(self):
        self.user_client = Client()


    def test_weather_page_content(self):
        url = reverse('weather:get_weather') + f'?city_name={CITIES[0]}'
        response = self.client.get(url)
        for content in PAGE_CONTENT:
            with self.subTest(content=content):
                self.assertIn(content, response.context)
    
    
    def test_404city_page_content(self):
        url = reverse('weather:get_weather') + f'?city_name={WRONG_CITY}'
        response = self.client.get(url)
        for content in PAGE404_CONTENT:
            with self.subTest(content=content):
                self.assertIn(content, response.context)

