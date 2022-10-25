from rest_framework import generics

from .models import Club
from .serializers import ClubSerializer


class ClubEnglishApiView(generics.ListAPIView,
                         generics.RetrieveAPIView):
    queryset = Club.objects.filter(language='english').all()
    serializer_class = ClubSerializer


class ClubRussianApiView(generics.ListAPIView,
                         generics.RetrieveAPIView):
    queryset = Club.objects.filter(language='russian').all()
    serializer_class = ClubSerializer
