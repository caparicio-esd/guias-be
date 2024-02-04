from rest_framework import generics

from guias.models import GuiaResources
from guias.serializers import GuiaResourcesSerializerMain


class GuiaResourcesViewList(generics.ListCreateAPIView):
    """
    GuiaResourcesView
    With RetrieveAPIView only GET requests are allowed with a id
    """
    queryset = GuiaResources.objects.all()
    serializer_class = GuiaResourcesSerializerMain


class GuiaResourcesViewSingle(generics.RetrieveUpdateDestroyAPIView):
    """
    GuiaResourcesView
    With RetrieveAPIView only GET requests are allowed with a id
    """
    queryset = GuiaResources.objects.all()
    serializer_class = GuiaResourcesSerializerMain
