from django.test import TestCase
from rest_framework.test import APIClient

from guias.models import Guia


# Create your tests here.
class GuiasTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.guia = Guia.objects.create(title="hola")

    def test_my_user(self):
        me = Guia.objects.all()
        self.assertEqual(len(me), 1)

    def test_guia_creation(self):
        response = self.client.get("/guias", HTTP_AUTHORIZATION="")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass
