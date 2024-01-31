import json
import pathlib

from guias.models import GuiaCompetencias


def run():
    # https://www.boe.es/eli/es/rd/2010/05/14/633/con
    cwd = pathlib.Path(__file__).parent.resolve()
    transversal_competencies_path = '{}/data/transversal_competencies.json'.format(cwd)
    general_competencies_path = '{}/data/general_competencies.json'.format(cwd)
    specific_competencies_path = '{}/data/specific_competencies.json'.format(cwd)
    mdi_competencies_path = '{}/data/mdi_competencies.json'.format(cwd)
    #
    GuiaCompetencias.objects.all().delete()
    #
    with open(transversal_competencies_path, 'r') as file:
        data = json.load(file)
        for competency in data:
            GuiaCompetencias.objects.create(**competency)
    with open(general_competencies_path, 'r') as file:
        data = json.load(file)
        for competency in data:
            GuiaCompetencias.objects.create(**competency)
    with open(specific_competencies_path, 'r') as file:
        data = json.load(file)
        for competency in data:
            GuiaCompetencias.objects.create(**competency)
    with open(mdi_competencies_path, 'r') as file:
        data = json.load(file)
        for competency in data:
            GuiaCompetencias.objects.create(**competency)
