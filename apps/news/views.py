from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.news.serializers import NewSerializer
from apps.news.models import New


class RetrieveNewApiViewSet(RetrieveModelMixin,
                            ListModelMixin,
                            GenericViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
