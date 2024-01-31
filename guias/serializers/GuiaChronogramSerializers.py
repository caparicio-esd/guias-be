from rest_framework import serializers

from guias.models import GuiaChronogramBlocks, GuiaChronogram


class GuiaChronogramBlocksSerializerMain(serializers.ModelSerializer):
    """
    GuiaChronogramBlocksSerializerMain
    Serializer for GuiaChronogramBlocks model with all fields
    """

    class Meta:
        model = GuiaChronogramBlocks
        fields = "__all__"


class GuiaChronogramSerializerMain(serializers.ModelSerializer):
    """
    GuiaChronogramBlocksSerializerMain
    Serializer for GuiaChronogramBlocks model with all fields
    """
    blocks = GuiaChronogramBlocksSerializerMain(many=True, read_only=True)

    class Meta:
        model = GuiaChronogram
        fields = "__all__"
