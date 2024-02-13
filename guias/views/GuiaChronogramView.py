from rest_framework import generics
from rest_framework.generics import get_object_or_404

from guias.models import GuiaChronogram, GuiaChronogramBlocks
from guias.serializers.GuiaChronogramSerializers import GuiaChronogramSerializerMain, GuiaChronogramBlocksSerializerMain


class GuiaChronogramSingleView(generics.RetrieveUpdateDestroyAPIView):
    """
    GuiaChronogramView
    With RetrieveAPIView only GET requests are allowed with a id
    """
    queryset = GuiaChronogram.objects.all()
    serializer_class = GuiaChronogramSerializerMain


class GuiaChronogramListView(generics.ListCreateAPIView):
    """
    GuiaChronogramView
    With RetrieveAPIView only GET requests are allowed with a id
    """
    queryset = GuiaChronogram.objects.all()
    serializer_class = GuiaChronogramSerializerMain


class GuiaChronogramBlockListView(generics.RetrieveAPIView):
    """
    GuiaChronogramView
    With RetrieveAPIView only GET requests are allowed with a id
    """
    queryset = GuiaChronogram.objects.all()
    serializer_class = GuiaChronogramSerializerMain


class GuiaChronogramBlockView(generics.RetrieveUpdateDestroyAPIView):
    """
    GuiaChronogramBlockView
    With RetrieveUpdateDestroyAPIView only GET requests are allowed with a id
    """
    queryset = GuiaChronogramBlocks.objects.all()
    serializer_class = GuiaChronogramBlocksSerializerMain


class GuiaChronogramBlockByChronogramSingleView(generics.RetrieveUpdateDestroyAPIView):
    """
    GuiaChronogramBlockByChronogramSingleView
    With RetrieveUpdateDestroyAPIView only GET requests are allowed with a id
    """
    queryset = GuiaChronogramBlocks.objects.all()
    serializer_class = GuiaChronogramBlocksSerializerMain

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        pk = self.kwargs.get('pk')
        block = self.kwargs.get('block')
        obj = get_object_or_404(queryset, chronogram_id=pk, id=block)
        return obj


class GuiaChronogramBlockByChronogramListView(generics.ListCreateAPIView):
    """
    GuiaChronogramBlockByChronogramListView
    With RetrieveUpdateDestroyAPIView only GET requests are allowed with a id
    """
    queryset = GuiaChronogramBlocks.objects.all()
    serializer_class = GuiaChronogramBlocksSerializerMain

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        pk = self.kwargs.get('pk')
        block = self.kwargs.get('block')
        obj = get_object_or_404(queryset, chronogram_id=pk, id=block)
        return obj