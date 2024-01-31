from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializerSmall(serializers.ModelSerializer):
    """
    UserSerializerSmall
    Serializer for User Django model
    """

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserSerializerMain(serializers.ModelSerializer):
    """
    UserSerializerMain
    Serializer for User Django model
    """

    class Meta:
        model = User
        fields = "__all__"
