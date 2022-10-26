from rest_framework.generics import ListAPIView

from apps.socials.models import Social
from apps.socials.serializers import SocialSerializer


class ListSocialApi(ListAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
