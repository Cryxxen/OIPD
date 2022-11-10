from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.partners.models import Partner
from apps.partners.serializers import PartnerSerializer


class PartnerApiViewSet(RetrieveModelMixin,
                        ListModelMixin,
                        GenericViewSet):

    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    pagination_class = None
