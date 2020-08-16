from django.test import TestCase
import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_GET_request(self):
        # Issue a GET request.
        response = self.client.get('/weather/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_POST_request_with_city(self):
        response = self.client.post('/weather/', {'city': '2222'})
        print(response.__dict__)
        self.assertEqual(response.status_code, 302)

    def test_POST_request_with_coord(self):
        pass
