from rest_framework import serializers

from guias.models import GuiaCompetencies


class GuiaCompetenciesSerializerMain(serializers.ModelSerializer):
    """
    GuiaCompetenciasSerializerMain
    Serializer for GuiaCompetencies model with all fields
    """

    class Meta:
        model = GuiaCompetencies
        fields = "__all__"
