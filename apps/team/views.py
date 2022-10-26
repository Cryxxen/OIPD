from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.team.models import Team
from apps.team.serializers import TeamSerializer


class RetrieveTeam(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ListTeam(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
