from rest_framework import viewsets

from apps.news.serializers import NewSerializer, NewImageSerializer
from apps.news.models import New, NewImage


class NewApiViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class NewImageApiViewSet(viewsets.ModelViewSet):
    queryset = NewImage.objects.all()
    serializer_class = NewImageSerializer
