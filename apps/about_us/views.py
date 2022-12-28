import logging

from rest_framework import generics

from apps.about_us import models, serialziers

logger = logging.getLogger('django')


class AboutUsApiView(generics.ListAPIView):
    queryset = models.AboutUs.objects.all()
    serializer_class = serialziers.AboutUsSerializer


class AboutPartnersApiViewSet(generics.ListAPIView):
    queryset = models.AboutPartners.objects.all()
    serializer_class = serialziers.AboutPartnersSerializer


class AboutTeamApiViewSet(generics.ListAPIView):
    queryset = models.AboutTeam.objects.all()
    serializer_class = serialziers.AboutTeamSerializer
