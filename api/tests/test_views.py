from pprint import pprint
from unittest import TestCase

from api.views import app

class TestAPIIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_GET_api_root_endpoint(self):
        response = self.app.get('/api/')

        self.assertDictEqual(response.json, {'results': None})