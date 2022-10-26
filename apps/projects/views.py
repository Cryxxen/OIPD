from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.projects.serializers import ProjectSerializer
from apps.projects.models import Project


class RetrieveProject(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ListProject(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
