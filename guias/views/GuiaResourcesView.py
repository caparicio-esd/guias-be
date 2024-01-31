from rest_framework import generics

from guias.models import GuiaResources
from guias.serializers import GuiaResourcesSerializerMain


class GuiaResourcesView(generics.RetrieveAPIView):
    """
    GuiaResourcesView
    With RetrieveAPIView only GET requests are allowed with a id
    """
    queryset = GuiaResources.objects.all()
    serializer_class = GuiaResourcesSerializerMain

