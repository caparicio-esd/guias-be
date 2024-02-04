from rest_framework import generics

from guias.models import GuiaContents
from guias.serializers import GuiaContentsSerializerMain


class GuiaContentsViewSingle(generics.RetrieveUpdateDestroyAPIView):
    """
    GuiaContentsViewSingle
    With RetrieveUpdateDestroyAPIView GET, DELETE and PUT methods are allowed with id
    """
    queryset = GuiaContents.objects.all()
    serializer_class = GuiaContentsSerializerMain


class GuiaContentsViewList(generics.ListCreateAPIView):
    """
    GuiaContentsViewList
    With ListCreateAPIView only GET and POSTS requests are allowed
    """
    queryset = GuiaContents.objects.all()
    serializer_class = GuiaContentsSerializerMain
