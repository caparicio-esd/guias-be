from django.contrib.auth.models import User
from faker import Faker
from guias.models import GuiaSpecialty, Guia, GuiaChronogram, GuiaResults, \
    GuiaCompetencies, GuiaResources
from . import populate_results, populate_resources, populate_specialties, \
    populate_chronogramblock, populate_contents, populate_competencies
import os


def run():
    # os.system("python manage.py flush")
    user_1 = User.objects.create_superuser('admin', 'admin@admin', 'admin')
    user_2 = User.objects.create_user("carlos", "carlos@carlos.es", "carlos")
    user_3 = User.objects.create_user("miriam", "miriam@miriam.es", "miriam")
    populate_results.run()
    populate_resources.run()
    populate_specialties.run()
    populate_chronogramblock.run()
    populate_contents.run()
    populate_competencies.run()

    fake = Faker()
    guia = Guia.objects.create(
        title=fake.sentence(nb_words=6),
        year_code=2024,
        description=fake.sentence(nb_words=20),
        identifier_type="test",
        identifier_character="test",
        identifier_specialty=GuiaSpecialty.objects.get(id=1),
        identifier_subject=fake.sentence(nb_words=2),
        identifier_course="1",
        identifier_semester="2",
        identifier_credits=10,
        identifier_hours_total=10,
        identifier_hours_presence=10,
        identifier_department=fake.sentence(nb_words=1),
        identifier_prelation=fake.sentence(nb_words=10),
        identifier_language="test",
        coordinator=user_1,
        chronogram=GuiaChronogram.objects.get(id=1),
    )
    guia.teachers.set([user_2, user_3])
    guia.results.set(GuiaResults.objects.filter(id__in=[2, 4, 5]))
    guia.competencies.set(GuiaCompetencies.objects.filter(id__in=[2, 4, 5, 10, 11, 13]))
    guia.resources.set(GuiaResources.objects.filter(id__in=[1, 2, 3, 4]))

