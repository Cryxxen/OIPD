from rest_framework import viewsets

from apps.team.models import Team
from apps.team.serializers import TeamSerializer


class EnglishTeamApiViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.filter(language='english').all()
    serializer_class = TeamSerializer


class RussianTeamApiViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.filter(language='russian').all()
    serializer_class = TeamSerializer
