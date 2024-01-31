from rest_framework import serializers

from guias.models import GuiaResources


class GuiaResourcesSerializerMain(serializers.ModelSerializer):
    """
    GuiaResourcesSerializerMain
    Serializer for GuiaResults model with all fields
    """

    class Meta:
        model = GuiaResources
        fields = "__all__"
