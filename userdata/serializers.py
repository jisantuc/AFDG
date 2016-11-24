from rest_framework import serializers

from userdata.models import AFDGUser

class AFDGUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AFDGUser
        fields = '__all__'
