from django.shortcuts import render

from rest_framework import viewsets

from userdata.models import AFDGUser
from userdata.serializers import AFDGUserSerializer


class AFDGUserViewSet(viewsets.ModelViewSet):
    queryset = AFDGUser.objects.all()
    serializer_class = AFDGUserSerializer
