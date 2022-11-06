from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class ListGame(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RetrieveGame(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
