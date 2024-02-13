from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from guias.models import Guia
from scripts import populate_guia


# Create your tests here.
class GuiaTest(TestCase):
    def setUp(self):
        if Guia.objects.count() is 0:
            populate_guia.run()
        self.client = APIClient()

    def test_get_endpoints(self):
        response = self.client.get("/guias/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get("/guias/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get("/guias/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_endpoints(self):
        response_data = {"title": "test", "course_code": "test", "year_code": 2024, "identifier_specialty": 1}
        response = self.client.post("/guias/", data=response_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_endpoints(self):
        response_data = {"title": "test"}
        response = self.client.put("/guias/1/", data=response_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_endpoints(self):
        response_data = {"title": "testtest"}
        response = self.client.patch("/guias/1/", data=response_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_delete_endpoints(self):
        #
        response = self.client.delete("/guias/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #
        response = self.client.get("/guias/1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
