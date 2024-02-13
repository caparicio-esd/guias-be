from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from guias.models import GuiaResources
from scripts import populate_resources


class GuiaResourcesTest(TestCase):
    def setUp(self):
        if GuiaResources.objects.count() is 0:
            populate_resources.run()
        self.client = APIClient()

    def test_get_endpoints(self):
        #
        response = self.client.get("/resources/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 5)
        #
        response = self.client.get("/resources/1/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertTrue("Dominando Wor" in data["title"])
        self.assertEqual(data["type"], 1)
        self.assertEqual(data["year"], None)

    def test_post_endpoints(self):
        #
        request_data = {"title": "Diseño Test", "description": "Test", "type": 1}
        response = self.client.post("/resources/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["id"], 6)
        self.assertEqual(data["title"], "Diseño Test")
        self.assertEqual(data["description"], "Test")
        self.assertEqual(data["type"], 1)
        #
        request_data = {"title": "Diseño Test"}
        response = self.client.post("/resources/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data["type"], ['This field is required.'])

    def test_put_endpoints(self):
        request_data = {"title": "Diseño Test Changed", "description": "Test Changed", "type": 1}
        response = self.client.put("/resources/4/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["id"], 4)
        self.assertEqual(data["title"], "Diseño Test Changed")
        self.assertEqual(data["description"], "Test Changed")
        self.assertEqual(data["type"], 1)

    def test_patch_endpoints(self):
        request_data = {"title": "Diseño Test Changed", "description": "Test Changed"}
        response = self.client.put("/resources/4/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data["type"],  ['This field is required.'])

    def test_delete_endpoints(self):
        #
        response = self.client.delete("/resources/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #
        response = self.client.get("/resources/1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
    