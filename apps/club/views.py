from rest_framework import generics

from .models import Club
from .serializers import ClubSerializer


class ListClubApiView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class RetrieveClubAPIView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
