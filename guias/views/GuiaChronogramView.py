from rest_framework import generics

from guias.models import GuiaChronogram
from guias.serializers.GuiaChronogramSerializers import GuiaChronogramSerializerMain


class GuiaChronogramView(generics.RetrieveAPIView):
    """
    GuiaChronogramView
    With RetrieveAPIView only GET requests are allowed with a id
    """
    queryset = GuiaChronogram.objects.all()
    serializer_class = GuiaChronogramSerializerMain
