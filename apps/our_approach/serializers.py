from rest_framework import serializers

from apps.our_approach.models import OurApproach


class OurApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurApproach
        fields = "__all__"
