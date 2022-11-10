from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.news.serializers import NewSerializer
from apps.news.models import New
from utils.custom_pagination_classes import CustomPageFivePaginationClass


class RetrieveNewApiViewSet(RetrieveModelMixin,
                            ListModelMixin,
                            GenericViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    pagination_class = CustomPageFivePaginationClass
