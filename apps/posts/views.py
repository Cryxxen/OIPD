from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from utils.custom_pagination_classes import CustomPageEightPaginationClass


class ListPost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPageEightPaginationClass


class RetrievePost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
