import json
import pathlib

from guias.models.GuiaResults import GuiaResults


def run():
    cwd = pathlib.Path(__file__).parent.resolve()
    results_path = '{}/data/resultados.json'.format(cwd)
    GuiaResults.objects.all().delete()

    with open(results_path) as f:
        results = json.load(f)
        for (i, result) in enumerate(results):
            [title, description] = result['title'], result['description']
            GuiaResults.objects.create(title=title, description=description, priority=i)
