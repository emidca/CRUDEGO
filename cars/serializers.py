from rest_framework import serializers
from .models import Car, Description


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ("id", "text")


class CarSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ("id", "name", "price", "model", "descriptions")
