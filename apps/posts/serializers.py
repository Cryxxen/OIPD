from rest_framework.serializers import ModelSerializer

from apps.posts.models import Post, PostType


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostTypeSerializer(ModelSerializer):
    post_type = PostSerializer(many=True, read_only=True)

    class Meta:
        model = PostType
        fields = "__all__"