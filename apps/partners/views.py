from rest_framework import viewsets

from apps.partners.models import Partner
from apps.partners.serializers import PartnerSerializer


class EnglishPartnerApiViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.filter(language='english').all()
    serializer_class = PartnerSerializer


class RussianPartnerApiViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.filter(language='russian').all()
    serializer_class = PartnerSerializer
