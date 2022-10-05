from rest_framework import viewsets

from apps.libraries.models import Library
from apps.libraries.serializers import LibrarySerializer


class LibraryApiViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
