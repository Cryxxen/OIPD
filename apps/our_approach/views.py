from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.our_approach.models import OurApproach
from apps.our_approach.serializers import OurApproachSerializer


class OurApproachViewSet(RetrieveModelMixin,
                         ListModelMixin,
                         GenericViewSet):
    queryset = OurApproach.objects.all()
    serializer_class = OurApproachSerializer
