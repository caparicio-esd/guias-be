from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from guias.models import GuiaContents
from scripts import populate_contents


class GuiaContentsTest(TestCase):
    def setUp(self):
        if GuiaContents.objects.count() is 0:
            populate_contents.run()
        self.client = APIClient()

    def test_get_endpoints(self):
        #
        response = self.client.get("/contents/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 21)
        #
        response = self.client.get("/contents/1/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertTrue("Arquitectura" in data["title"])
        self.assertEqual(data["priority"], 0)
        self.assertEqual(data["parent"], None)
        #
        response = self.client.get("/contents/2/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertTrue("¿Qué es" in data["title"])
        self.assertEqual(data["priority"], 0)
        self.assertEqual(data["parent"], 1)

    def test_post_endpoints(self):
        #
        request_data = {"title": "Diseño Test", "priority": 1, "parent": 1}
        response = self.client.post("/contents/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["id"], 22)
        self.assertEqual(data["title"], "Diseño Test")
        self.assertEqual(data["priority"], 1)
        self.assertEqual(data["parent"], 1)
        #
        request_data = {"title": "Diseño Test", "priority": 1, "parent": 100}
        response = self.client.post("/contents/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data["parent"], ['Invalid pk "100" - object does not exist.'])

    def test_put_endpoints(self):
        request_data = {"title": "Diseño Test Changed", "priority": 2, "parent": 1}
        response = self.client.put("/contents/4/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["id"], 4)
        self.assertEqual(data["title"], "Diseño Test Changed")
        self.assertEqual(data["priority"], 2)
        self.assertEqual(data["parent"], 1)

    def test_patch_endpoints(self):
        request_data = {"priority": 3}
        response = self.client.patch("/contents/4/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["id"], 4)
        self.assertEqual(data["priority"], 3)
        self.assertEqual(data["parent"], 3)

    def test_delete_endpoints(self):
        #
        response = self.client.delete("/contents/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #
        response = self.client.get("/contents/1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
    