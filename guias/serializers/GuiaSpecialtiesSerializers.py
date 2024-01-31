from rest_framework import serializers

from guias.models import GuiaSpecialty


class GuiaSpecialtySerializerMain(serializers.ModelSerializer):
    """
    GuiaSpecialtySerializerMain
    Serializer GuiaSpecialty with all fields
    """

    class Meta:
        model = GuiaSpecialty
        fields = "__all__"
