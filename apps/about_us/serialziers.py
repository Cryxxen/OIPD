from rest_framework import serializers

from apps.about_us import models


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutUs
        fields = "__all__"


class AboutPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutPartners
        fields = "__all__"

class AboutTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutTeam
        fields = "__all__"