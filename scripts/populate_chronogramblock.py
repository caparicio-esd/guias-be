import json
import pathlib

from guias.models import GuiaChronogramBlocks, GuiaChronogram


# TODO improve block - theme relation
def run():
    cwd = pathlib.Path(__file__).parent.resolve()
    chronogram_path = '{}/data/guia_chronogram.json'.format(cwd)
    #
    GuiaChronogramBlocks.objects.all().delete()
    GuiaChronogram.objects.all().delete()
    chronogram = GuiaChronogram.objects.create()
    #
    with open(chronogram_path, 'r') as file:
        data = json.load(file)
        for competency in data:
            competency["chronogram"] = chronogram
            GuiaChronogramBlocks.objects.create(**competency)
