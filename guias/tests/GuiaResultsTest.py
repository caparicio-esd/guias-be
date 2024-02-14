from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from guias.models import GuiaResults
from scripts import populate_results


class GuiaResultsTest(TestCase):
    def setUp(self):
        if GuiaResults.objects.count() is 0:
            populate_results.run()
        self.client = APIClient()

    def test_get_endpoints(self):
        #
        response = self.client.get("/api/v1/results/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 6)
        #
        response = self.client.get("/api/v1/results/1/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertTrue("El alumno será capaz " in data["title"])
        self.assertEqual(data["priority"], 0)

    def test_post_endpoints(self):
        #
        request_data = {"title": "Diseño Test", "description": "Test", "priority": 1}
        response = self.client.post("/api/v1/results/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["id"], 7)
        self.assertEqual(data["title"], "Diseño Test")
        self.assertEqual(data["description"], "Test")
        self.assertEqual(data["priority"], 1)
        #
        request_data = {"title": "Diseño Test"}
        response = self.client.post("/api/v1/results/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["priority"], 1)
        self.assertEqual(data["description"], "")

    def test_put_endpoints(self):
        request_data = {"title": "Diseño Test Changed", "description": "Test Changed", "priority": 10}
        response = self.client.put("/api/v1/results/4/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["id"], 4)
        self.assertEqual(data["title"], "Diseño Test Changed")
        self.assertEqual(data["description"], "Test Changed")
        self.assertEqual(data["priority"], 10)

    def test_patch_endpoints(self):
        request_data = {"title": "Diseño Test Changed", "description": "Test Changed"}
        response = self.client.patch("/api/v1/results/3/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["id"], 3)
        self.assertEqual(data["title"], "Diseño Test Changed")
        self.assertEqual(data["description"], "Test Changed")
        self.assertEqual(data["priority"], 2)

    def test_delete_endpoints(self):
        #
        response = self.client.delete("/api/v1/results/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #
        response = self.client.get("/api/v1/results/1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
    