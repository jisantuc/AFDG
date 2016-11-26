from rest_framework import serializers

from game.models import AFDGGame


class AFDGGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AFDGGame
        fields = '__all__'
