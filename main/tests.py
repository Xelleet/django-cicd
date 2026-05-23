from django.test import TestCase, Client
from django.urls import reverse


class CalculatorTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_get_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_addition(self):
        response = self.client.post(self.url, {
            'num1': '5',
            'num2': '3'
        })
        self.assertEqual(response.context['result'], 8)
