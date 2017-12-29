"""Mixins and helper classes"""

from rest_framework import authentication, exceptions
from rest_framework.viewsets import GenericViewSet

from django.contrib.auth.models import User


class UniqueUserAuthentication(authentication.BaseAuthentication):
    """Authentication class to authenticate as long as a user is provided"""

    def authenticate(self, request):
        users = User.objects.filter(
            username=request.data['username']
        )
        if not users or users[0].password == request.data['password']:
            user, _ = User.objects.get_or_create(**request.data)
            return (user, None)
        elif users[0].password != request.data['password']:
            raise exceptions.AuthenticationFailed(
                'Password incorrect or username already exists'
            )
        else:
            return None


class TrustViewSetMixIn(GenericViewSet):
    authentication_classes = (UniqueUserAuthentication,)

    class Meta:
        abstract = True
