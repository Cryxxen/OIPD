import logging

from rest_framework import generics

from apps.about_us.models import AboutUs
from apps.about_us.serialziers import AboutUsSerializer

logger = logging.getLogger('django')


class AboutUsApiView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def get(self, request, *args, **kwargs):
        print(request.method)
        logger.info(request.method)
        return self.list(request, *args, **kwargs)