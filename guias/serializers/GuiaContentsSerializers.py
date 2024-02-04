from rest_framework import serializers

from guias.models import GuiaContents


class GuiaContentsSerializerMain(serializers.ModelSerializer):
    """
    GuiaContentsSerializerMain
    Serializer for GuiaCompetencies model with all fields
    """

    class Meta:
        model = GuiaContents
        fields = "__all__"
