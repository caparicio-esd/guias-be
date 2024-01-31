from rest_framework import generics

from guias.models import GuiaResults
from guias.serializers.GuiaResultsSerializers import GuiaResultsSerializerMain


class GuiaResultsView(generics.RetrieveAPIView):
    """
    GuiaResultsView
    With RetrieveAPIView only GET requests are allowed with a id
    """
    queryset = GuiaResults.objects.all()
    serializer_class = GuiaResultsSerializerMain

