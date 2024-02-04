from rest_framework import generics

from guias.models import GuiaResults, GuiaSpecialty
from guias.serializers import GuiaSpecialtySerializerMain


class GuiaSpecialtiesViewSingle(generics.RetrieveUpdateDestroyAPIView):
    """
    GuiaResultsViewSingle
    With RetrieveUpdateDestroyAPIView GET, DELETE and PUT methods are allowed with id
    """
    queryset = GuiaSpecialty.objects.all()
    serializer_class = GuiaSpecialtySerializerMain


class GuiaSpecialtiesViewList(generics.ListCreateAPIView):
    """
    GuiaSpecialtiesViewList
    With ListCreateAPIView only GET and POSTS requests are allowed
    """
    queryset = GuiaSpecialty.objects.all()
    serializer_class = GuiaSpecialtySerializerMain


