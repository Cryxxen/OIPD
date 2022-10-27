from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.team.models import Team
from apps.team.serializers import TeamSerializer


class TeamApiViewSet(RetrieveModelMixin,
                     ListModelMixin,
                     GenericViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
