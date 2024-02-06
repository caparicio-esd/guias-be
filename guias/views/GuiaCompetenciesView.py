from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status

from guias.models import GuiaCompetencies
from guias.serializers.GuiaCompetenciesSerializers import GuiaCompetenciesSerializerMain


class GuiaCompetenciasView(generics.ListCreateAPIView):
    """
    GuiaCompetenciasView
    View for listing GuiaCompetencias model
    for endpoint /competencias
    """
    queryset = GuiaCompetencies.objects.all()
    serializer_class = GuiaCompetenciesSerializerMain
    lookup_field = "__all__"


class GuiaCompetenciasListView(generics.ListAPIView):
    """
    GuiaCompetenciasListView
    View for listing GuiaCompetencias model based in comma separated list of ids
    for endpoint /competencias/list/<id>,<id>,<id>,<id>
    """
    def get(self, request, *args, **kwargs):
        ids = kwargs.get('ids', '')
        id_list = ids.split(',')
        try:
            id_list = [int(id) for id in id_list]
        except ValueError:
            return JsonResponse({"error": "Invalid ID format"}, status=status.HTTP_400_BAD_REQUEST)
        queryset = GuiaCompetencies.objects.filter(id__in=id_list)
        serializer = GuiaCompetenciesSerializerMain(queryset, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


class GuiaCompetenciasSingleView(generics.RetrieveUpdateDestroyAPIView):
    """
    GuiaCompetenciasSingleView
    View for retrieving a single GuiaCompetencia model by id
    for endpoint /competencias/<id>
    """
    queryset = GuiaCompetencies.objects.all()
    serializer_class = GuiaCompetenciesSerializerMain
    lookup_field = "id"


class GuiaCompetenciasSingleViewByKey(generics.RetrieveAPIView):
    """
    GuiaCompetenciasSingleViewByKey
    View for retrieving a single GuiaCompetencia model by key
    for endpoint /competencias/<key>
    """
    queryset = GuiaCompetencies.objects.all()
    serializer_class = GuiaCompetenciesSerializerMain
    lookup_field = "key"
