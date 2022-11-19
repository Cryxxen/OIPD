from rest_framework.serializers import ModelSerializer

from apps.posts.models import Post, PostType, PostSocial


class PostSocialSerializer(ModelSerializer):
    class Meta:
        model = PostSocial
        fields = "__all__"


class PostSerializer(ModelSerializer):
    post_socials = PostSocialSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class PostTypeSerializer(ModelSerializer):
    post_type = PostSerializer(many=True, read_only=True)

    class Meta:
        model = PostType
        fields = "__all__"
