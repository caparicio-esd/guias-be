from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from scripts import populate_chronogramblock
from scripts import populate_contents
from scripts import populate_results
from scripts import populate_competencies
from scripts import populate_guia


# Create your tests here.
class GuiaTest(TestCase):
    def setUp(self):
        populate_guia.run()
        self.client = APIClient()

    def test_guia_url_exists(self):
        response = self.client.get("/guias")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get("/guias/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get("/guias/4")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_guia_fields(self):
        pass

    def tearDown(self):
        pass
