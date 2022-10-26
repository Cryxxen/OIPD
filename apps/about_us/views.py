from rest_framework import viewsets, generics

from apps.about_us.models import AboutUs
from apps.about_us.serialziers import AboutUsSerializer


class AboutUsApiView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

