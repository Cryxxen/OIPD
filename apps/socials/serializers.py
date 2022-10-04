from rest_framework import serializers

from apps.socials.models import Social


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
