from django.test import TestCase, Client
from django.urls import reverse


class CalculatorViewTests(TestCase):

    def test_index_post_valid_data(self):
        response = self.client.post(self.url, {
            'num1': '5',
            'num2': '3'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.context['result'], 8)