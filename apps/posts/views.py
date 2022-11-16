from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.posts.models import Post, PostType
from apps.posts.serializers import PostSerializer, PostTypeSerializer
from utils.custom_pagination_classes import CustomPageEightPaginationClass


class ListPost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPageEightPaginationClass


class RetrievePost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class ListPostType(ListAPIView):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer