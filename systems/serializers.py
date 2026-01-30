from rest_framework import serializers
from .models import System

class SystemReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = System
        fields = "__all__"

class SystemWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = System
        fields = ["name", "description"]
        