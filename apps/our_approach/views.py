from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.our_approach.models import OurApproach
from apps.our_approach.serializers import OurApproachSerializer


class ListOurApproach(ListAPIView):
    queryset = OurApproach.objects.all()
    serializer_class = OurApproachSerializer


class RetrieveOurApproach(RetrieveAPIView):
    queryset = OurApproach.objects.all()
    serializer_class = OurApproachSerializer
