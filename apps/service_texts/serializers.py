from rest_framework.serializers import ModelSerializer

from apps.service_texts.models import ServiceText


class ServiceTextSerializer(ModelSerializer):
    class Meta:
        model = ServiceText
        fields = "__all__"
