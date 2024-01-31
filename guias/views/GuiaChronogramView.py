from rest_framework import generics

from guias.models import GuiaChronogram


class GuiaChronogramView(generics.RetrieveAPIView):
    queryset = GuiaChronogram.objects.all()
