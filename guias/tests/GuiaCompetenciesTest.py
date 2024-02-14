from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from guias.models import GuiaCompetencies
from scripts import populate_competencies


class GuiaCompetenciesTest(TestCase):
    def setUp(self):
        if GuiaCompetencies.objects.count() is 0:
            populate_competencies.run()
        self.client = APIClient()

    def test_get_endpoints(self):
        #
        response = self.client.get("/api/v1/competencies/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 118)
        #
        response = self.client.get("/api/v1/competencies/1/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertTrue("Organizar y planificar" in data["title"])
        self.assertEqual(data["type"], "transversal")
        self.assertEqual(data["key"], "CT1")
        #
        response = self.client.get("/api/v1/competencies/CT1/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertTrue("Organizar y planificar" in data["title"])
        self.assertEqual(data["type"], "transversal")
        self.assertEqual(data["key"], "CT1")
        #
        response = self.client.get("/api/v1/competencies/list/1,2,3/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 3)

    def test_post_endpoints(self):
        #
        request_data = {"title": "Diseño Test", "key": "TEST1", "specialty": "test", "type": "test"}
        response = self.client.post("/api/v1/competencies/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["id"], 119)
        self.assertEqual(data["title"], "Diseño Test")
        self.assertEqual(data["key"], "TEST1")
        self.assertEqual(data["specialty"], "test")
        #
        request_data = {"title": "Diseño Test"}
        response = self.client.post("/api/v1/competencies/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data["key"], ['This field is required.'])
        self.assertEqual(data["type"], ['This field is required.'])
        self.assertEqual(data["specialty"], ['This field is required.'])

    def test_put_endpoints(self):
        request_data = {"title": "Diseño Test", "key": "TEST1", "specialty": "test", "type": "test"}
        response = self.client.put("/api/v1/competencies/1/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], "Diseño Test")
        self.assertEqual(data["key"], "TEST1")
        self.assertEqual(data["specialty"], "test")

    def test_patch_endpoints(self):
        #
        request_data = {"key": "CT1"}
        response = self.client.patch("/api/v1/competencies/4/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data["key"], ['guia competencies with this key already exists.'])
        #
        request_data = {"key": "TEST"}
        response = self.client.patch("/competencies/4/", data=request_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["id"], 4)
        self.assertEqual(data["key"], "TEST")

    def test_delete_endpoints(self):
        #
        response = self.client.delete("/api/v1/competencies/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #
        response = self.client.get("/api/v1/competencies/1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
