from rest_framework import viewsets, status
from rest_framework.response import Response

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from afdg_core.mixins import TrustViewSetMixIn

from userdata.models import UserWinTracker
from userdata.serializers import (
    UserWinTrackerSerializer,
    UserSerializer
)


class UserViewSet(TrustViewSetMixIn, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        """Override to get or create the user's token"""

        user = User.objects.get(
            username=request.data['username'],
            password=request.data['password']
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            resp = Response({'token': token.key}, status=status.HTTP_200_OK) 
        else:
            resp = Response(status=status.HTTP_401_NOT_AUTHORIZED)
        return resp


class UserWinTrackerViewSet(TrustViewSetMixIn, viewsets.ModelViewSet):
    queryset = UserWinTracker.objects.all()
    serializer_class = UserWinTrackerSerializer
