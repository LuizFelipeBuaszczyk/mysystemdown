from rest_framework import serializers
from systems.models import Bot

class BotReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ["id", "bot_name", "api_token"]

class BotWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ["bot_name"]