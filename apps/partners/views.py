from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.partners.models import Partner
from apps.partners.serializers import PartnerSerializer


class RetrievePartner(RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class ListPartner(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
