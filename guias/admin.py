from django.contrib import admin

from guias.models import Guia, GuiaField

# Register your models here.
admin.site.register(Guia)
admin.site.register(GuiaField)

