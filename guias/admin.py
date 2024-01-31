from django.contrib import admin


# TODO migrar a carpetitas
from guias.models import Guia, GuiaCompetencies, GuiaSpecialty, GuiaContents, GuiaResults, GuiaResources

# Register your models here.
admin.site.register(Guia)
admin.site.register(GuiaSpecialty)
admin.site.register(GuiaCompetencies)
admin.site.register(GuiaResults)
admin.site.register(GuiaContents)
admin.site.register(GuiaResources)
