from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from guias.models import Guia
from guias.serializers.GuiaSerializers import GuiaSerializerMain, GuiaSerializerSmall, GuiaSerializerMainPost


class GuiaViewList(APIView):
    def get(self, request):
        guias = Guia.objects.all()
        serializer = GuiaSerializerSmall(guias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuiaSerializerMainPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuiaViewSingle(APIView):
    def _get_guia(self, guia_id):
        try:
            guia = Guia.objects.get(id=guia_id)
            return guia
        except Guia.DoesNotExist:
            raise Http404

    def get(self, request, guia_id):
        serializer = GuiaSerializerMain(self._get_guia(guia_id))
        return Response(serializer.data)

    def put(self, request: Request, guia_id):
        serializer = GuiaSerializerMainPost(self._get_guia(guia_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, guia_id):
        serializer = GuiaSerializerMainPost(self._get_guia(guia_id), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, guia_id):
        self._get_guia(guia_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
