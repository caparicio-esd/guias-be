import pytest
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from scripts import populate_specialties


class GuiaSpecialtiesTest(TestCase):
    def setUp(self):
        populate_specialties.run()
        self.client = APIClient()

    def test_get_endpoints(self):
        #
        response = self.client.get("/specialties/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 4)
        #
        response = self.client.get("/specialties/1/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["title"], "Diseño Gráfico")
        self.assertEqual(data["description"], "Blabla")

    def test_post_endpoints(self):
        request_data = {"title": "Diseño Test", "description": "Test"}
        response = self.client.post("/specialties/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["id"], 5)
        self.assertEqual(data["title"], "Diseño Test")
        self.assertEqual(data["description"], "Test")

    def test_put_endpoints(self):
        request_data = {"title": "Diseño Test Changed", "description": "Test Changed"}
        response = self.client.put("/specialties/4/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["id"], 4)
        self.assertEqual(data["title"], "Diseño Test Changed")
        self.assertEqual(data["description"], "Test Changed")

    def test_patch_endpoints(self):
        request_data = {"title": "Diseño Test Changed partially"}
        response = self.client.put("/specialties/4/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["description"], "Blabla")

    def test_delete_endpoints(self):
        #
        response = self.client.delete("/specialties/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #
        response = self.client.get("/specialties/1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
    