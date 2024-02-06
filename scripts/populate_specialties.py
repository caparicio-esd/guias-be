import json
import pathlib

from guias.models.GuiaSpecialty import GuiaSpecialty


def run():
    cwd = pathlib.Path(__file__).parent.resolve()
    specialties_path = '{}/data/specialties.json'.format(cwd)
    GuiaSpecialty.objects.all().delete()

    with open(specialties_path) as f:
        specialties = json.load(f)
        for specialty in specialties:
            [title, description] = specialty['title'], specialty['description']
            GuiaSpecialty.objects.create(title=title, description=description)
