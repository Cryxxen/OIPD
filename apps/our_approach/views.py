from rest_framework import viewsets

from apps.our_approach.models import OurApproach
from apps.our_approach.serializers import OurApproachSerializer


class EnglishOurApproachApiViewSet(viewsets.ModelViewSet):
    queryset = OurApproach.objects.filter(language='english').all()
    serializer_class = OurApproachSerializer


class RussianOurApproachApiViewSet(viewsets.ModelViewSet):
    queryset = OurApproach.objects.filter(language='russian').all()
    serializer_class = OurApproachSerializer
