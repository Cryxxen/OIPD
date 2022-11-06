from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.service_texts.models import ServiceText
from apps.service_texts.serializers import ServiceTextSerializer


class ServiceTextApiViewSet(GenericViewSet,
                            ListModelMixin):
    queryset = ServiceText.objects.all()
    serializer_class = ServiceTextSerializer
