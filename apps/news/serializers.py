from rest_framework import serializers

from apps.news.models import New, NewImage


class NewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewImage
        fields = "__all__"


class NewSerializer(serializers.ModelSerializer):
    images = NewImageSerializer(many=True, read_only=True)

    class Meta:
        model = New
        fields = (
            "id",
            "language",
            "image",
            "title",
            "create_at",
            "description",
            'images',
        )
