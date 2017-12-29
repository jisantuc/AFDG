from rest_framework import viewsets
from rest_framework.response import Response

from game.models import AFDGGame
from game.serializers import AFDGGameSerializer


class AFDGGameViewSet(viewsets.ModelViewSet):
    model = AFDGGame
    queryset = AFDGGame.objects.all()
    serializer_class = AFDGGameSerializer

    def list(self, request):
        return Response(
            self.queryset.filter(players=self.request.user)
        )
