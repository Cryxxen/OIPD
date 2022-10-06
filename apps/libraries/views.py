from rest_framework import viewsets

from apps.libraries.models import Library
from apps.libraries.serializers import LibrarySerializer


class EnglishLibraryApiViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.filter(language='english').all()
    serializer_class = LibrarySerializer


class RussianLibraryApiViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.filter(language='russian').all()
    serializer_class = LibrarySerializer
