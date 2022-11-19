from rest_framework import serializers

from apps.news.models import New, NewSocial


class NewSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewSocial
        fields = "__all__"


class NewSerializer(serializers.ModelSerializer):
    new_socials = NewSocialSerializer(many=True, read_only=True)

    class Meta:
        model = New
        fields = "__all__"
