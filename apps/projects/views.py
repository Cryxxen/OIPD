from rest_framework import viewsets

from apps.projects.serializers import ProjectSerializer
from apps.projects.models import Project


class EnglishProjectApiViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(language="english").all()
    serializer_class = ProjectSerializer


class RussianProjectApiViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(language='russian').all()
    serializer_class = ProjectSerializer
