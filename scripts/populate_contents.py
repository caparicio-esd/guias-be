import json
import pathlib

from guias.models.GuiaContents import GuiaContents


def run():
    cwd = pathlib.Path(__file__).parent.resolve()
    contents_path = '{}/data/contents.json'.format(cwd)
    GuiaContents.objects.all().delete()

    with open(contents_path) as f:
        contents = json.load(f)
        for (i, content) in enumerate(contents):
            title, parent, priority = content['title'], content['parent'], content['priority']
            o = GuiaContents.objects.create(title=title, parent=None, priority=i)
            for (j, child) in enumerate(content['children']):
                title_child, priority_child = child['title'], child['priority']
                GuiaContents.objects.create(title=title_child, parent=o, priority=j)
