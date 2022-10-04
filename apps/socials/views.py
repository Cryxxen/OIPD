from rest_framework import viewsets

from apps.socials.models import Social
from apps.socials.serializers import SocialSerializer


class SocialApiViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
