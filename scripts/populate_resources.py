import json
import pathlib

from guias.models.GuiaResources import GuiaResources


def run():
    cwd = pathlib.Path(__file__).parent.resolve()
    resources_path = '{}/data/resources.json'.format(cwd)
    GuiaResources.objects.all().delete()

    with open(resources_path) as f:
        resources = json.load(f)
        for resource in resources:
            GuiaResources.objects.create(
                title=resource["title"],
                description=resource["description"],
                author=resource["author"],
                editorial=resource["editorial"],
                href=resource["href"],
                type=resource["type"],
                year=resource["year"]
            )
