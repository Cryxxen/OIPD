from rest_framework import viewsets

from apps.about_us.models import AboutUs
from apps.about_us.serialziers import AboutUsSerializer


class EnglishAboutUsApiViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.filter(language='english').all()
    serializer_class = AboutUsSerializer


class RussianAboutUsApiViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.filter(language='russian').all()
    serializer_class = AboutUsSerializer
