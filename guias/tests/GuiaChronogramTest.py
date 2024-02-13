from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from guias.models import GuiaChronogram, GuiaChronogramBlocks
from scripts import populate_chronogramblock


class GuiaChronogramTest(TestCase):
    def setUp(self):
        if GuiaChronogram.objects.count() is 0 \
                and GuiaChronogramBlocks.objects.count() is 0:
            populate_chronogramblock.run()
        self.client = APIClient()

    def test_get_endpoints(self):
        #
        response = self.client.get("/chronograms/1/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertEqual(type(data["blocks"]), list)
        self.assertEqual(len(data["blocks"]), 18)
        self.assertEqual(data["blocks"][0]["block"], 1)
        self.assertEqual(data["blocks"][0]["chronogram"], 1)
        #
        response = self.client.get("/chronograms/1/chronogramblocks/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 18)
        #
        response = self.client.get("/chronograms/1/chronogramblocks/1/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["chronogram"], 1)

    def test_post_endpoints(self):
        response = self.client.post("/chronograms/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["blocks"], [])
        self.assertEqual(data["id"], 2)
        #
        response_data = {"time_entity": 1, "chronogram": 2, "block": 2, "theme": 2}
        response = self.client.post("/chronograms/2/chronogramblocks/", data=response_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["theme"], 2)
        self.assertEqual(data["competencies"], None)
        self.assertEqual(data["chronogram"], 2)

    def test_put_endpoints(self):
        response_data = {"time_entity": 1, "chronogram": 1, "block": 2, "theme": 2}
        response = self.client.put("/chronograms/1/chronogramblocks/1/", data=response_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["theme"], 2)
        self.assertEqual(data["chronogram"], 1)

    def test_patch_endpoints(self):
        response_data = {"time_entity": 1, "theme": 2}
        response = self.client.patch("/chronograms/1/chronogramblocks/1/", data=response_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["theme"], 2)
        self.assertEqual(data["chronogram"], 1)

    def test_delete_endpoints(self):
        #
        response = self.client.delete("/chronograms/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #
        response = self.client.get("/chronograms/1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
