import json

from django.test import TestCase
from rest_framework.test import APIClient

import scripts.populate_competencies

# Create your tests here.
class GuiasTests(TestCase):
    def setUp(self):
        # TODO set other scripts...
        scripts.populate_competencies.run()
        self.client = APIClient()

    def test_guia_url_exists(self):
        response = self.client.get("/guias")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/guias/1")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/guias/4")
        self.assertEqual(response.status_code, 404)

    def test_guia_competencias(self):
        response = self.client.get("/competencias/1")
        data = response.json()
        self.assertTrue("Organizar y planificar" in data["title"])
        self.assertEqual(data["key"], "CT1")
        self.assertEqual(data["type"], "transversal")
        self.assertEqual(data["specialty"], "transversal")
        self.assertEqual(data["description"], "")

    def test_guia_competencias_not_allowed_methods(self):
        response = self.client.post("/competencias", data={"title": "test", "description": "test"})
        self.assertEqual(response.status_code, 405)
        response = self.client.put("/competencias/1", data={"title": "test", "description": "test"})
        self.assertEqual(response.status_code, 405)
        response = self.client.delete("/competencias/1")
        self.assertEqual(response.status_code, 405)


    def test_get_guia_fields(self):
        pass

    def tearDown(self):
        pass
