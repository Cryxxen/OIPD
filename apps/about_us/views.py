from rest_framework import viewsets

from apps.about_us.models import AboutUs
from apps.about_us.serialziers import AboutUsSerializer


class AboutUsApiViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
