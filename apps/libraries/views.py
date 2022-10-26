from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.libraries.models import Library
from apps.libraries.serializers import LibrarySerializer


class RetrieveLibraryApiView(RetrieveAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class ListLibraryAPiView(ListAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
