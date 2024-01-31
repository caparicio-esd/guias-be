from django.contrib.auth.models import User
from faker import Faker
from guias.models import GuiaSpecialty, Guia, GuiaChronogram


def run():
    fake = Faker()
    guia_specialty_mother_01 = GuiaSpecialty.objects.create(
        title="guia_specialty_mother",
        description="guia_specialty_mother"
    )
    Guia.objects.create(
        title=fake.words(nb=5),
        year_code=2024,
        description="hola",
        identifier_type="test",
        identifier_character="test",
        identifier_specialty=guia_specialty_mother_01,
        identifier_subject="test",
        identifier_course="test",
        identifier_semester="test",
        identifier_credits=10,
        identifier_hours_total=10,
        identifier_hours_presence=10,
        identifier_department="test",
        identifier_prelation="test",
        identifier_language="test",
        coordinator=User.objects.get(id=1),
        chronogram=GuiaChronogram.objects.get(id=1),
    )
