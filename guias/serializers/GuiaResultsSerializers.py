from rest_framework import serializers

from guias.models import GuiaResults


class GuiaResultsSerializerMain(serializers.ModelSerializer):
    """
    GuiaResultsSerializerMain
    Serializer for GuiaResults model with all fields
    """

    class Meta:
        model = GuiaResults
        fields = "__all__"
