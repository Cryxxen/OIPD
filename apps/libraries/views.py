from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.libraries.models import Library
from apps.libraries.serializers import LibrarySerializer


class RetrieveLibraryApiViewSet(RetrieveModelMixin,
                                ListModelMixin,
                                GenericViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
