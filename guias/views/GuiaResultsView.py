from rest_framework import generics

from guias.models import GuiaResults
from guias.serializers.GuiaResultsSerializers import GuiaResultsSerializerMain


class GuiaResultsViewSingle(generics.RetrieveUpdateDestroyAPIView):
    """
    GuiaResultsViewSingle
    With RetrieveUpdateDestroyAPIView GET, DELETE and PUT methods are allowed with id
    """
    queryset = GuiaResults.objects.all()
    serializer_class = GuiaResultsSerializerMain


class GuiaResultsViewList(generics.ListCreateAPIView):
    """
    GuiaResultsView
    With ListCreateAPIView only GET and POSTS requests are allowed
    """
    queryset = GuiaResults.objects.all()
    serializer_class = GuiaResultsSerializerMain


