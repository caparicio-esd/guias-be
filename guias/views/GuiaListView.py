from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from guias.models import Guia
from guias.serializers.GuiaSerializers import GuiaSerializerMain


class GuiaListView(APIView):
    def get(self, request):
        guias = Guia.objects.all()
        serializer = GuiaSerializerMain(guias, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = GuiaSerializerMain(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)