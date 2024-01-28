from django.http import Http404, HttpResponse, JsonResponse
from .models import Guia
from .serializers import GuiaSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView


class GuiaListView(APIView):
    def get(self, request):
        guias = Guia.objects.all()
        serializer = GuiaSerializer(guias, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = GuiaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuiaSingleView(APIView):
    def _get_guia(self, guia_id):
        try:
            guia = Guia.objects.get(id=guia_id)
            return guia
        except Guia.DoesNotExist:
            raise Http404

    def get(self, request, guia_id):
        serializer = GuiaSerializer(self._get_guia(guia_id))
        return JsonResponse(serializer.data)

    def put(self, request, guia_id):
        data = JSONParser().parse(request)
        serializer = GuiaSerializer(self._get_guia(guia_id), data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, guia_id):
        self._get_guia(guia_id).delete()
        return HttpResponse(status=status.HTTP_202_ACCEPTED)
