from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from scripts import populate_chronogramblock
from scripts import populate_contents
from scripts import populate_resultados
from scripts import populate_competencies
from scripts import populate_guia


# Create your tests here.
class GuiaTest(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'admin@admin', 'admin')
        populate_competencies.run()
        populate_chronogramblock.run()
        populate_contents.run()
        populate_resultados.run()
        populate_guia.run()
        self.client = APIClient()

    def test_guia_url_exists(self):
        response = self.client.get("/guias")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get("/guias/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get("/guias/4")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

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
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put("/competencias/1", data={"title": "test", "description": "test"})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.delete("/competencias/1")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_guia_fields(self):
        pass

    def tearDown(self):
        pass
