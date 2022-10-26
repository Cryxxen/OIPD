from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.games.models import Game
from apps.games.serializers import GameSerializer


class ListGame(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class RetrieveGame(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
