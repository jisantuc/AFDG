from rest_framework import serializers

from django.contrib.auth.models import User

from userdata.models import UserWinTracker


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_staff', 'is_superuser')


class UserWinTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWinTracker
        fields = '__all__'
