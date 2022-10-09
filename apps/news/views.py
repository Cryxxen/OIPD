from rest_framework import viewsets

from apps.news.serializers import NewSerializer
from apps.news.models import New


class EnglishNewApiViewSet(viewsets.ModelViewSet):
    queryset = New.objects.filter(language='english').all()
    serializer_class = NewSerializer


class RussianNewApiViewSet(viewsets.ModelViewSet):
    queryset = New.objects.filter(language='russian').all()
    serializer_class = NewSerializer
