from rest_framework import viewsets

from apps.partners.models import Partner
from apps.partners.serializers import PartnerSerializer


class PartnerApiViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
