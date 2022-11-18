from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from apps.posts.models import Post, PostType
from apps.posts.serializers import PostSerializer, PostTypeSerializer
from utils.custom_pagination_classes import CustomPageEightPaginationClass


class PostApiViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPageEightPaginationClass


class ListPostType(GenericViewSet,
                   ListModelMixin):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
