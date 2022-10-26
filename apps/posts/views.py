from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.posts.models import Post
from apps.posts.serializers import GameSerializer


class ListGame(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = GameSerializer


class RetrieveGame(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = GameSerializer
