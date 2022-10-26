from rest_framework.serializers import ModelSerializer

from apps.posts.models import Post


class GameSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
