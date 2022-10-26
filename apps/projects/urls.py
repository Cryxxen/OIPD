from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.projects.views import ListProject, RetrieveProject


urlpatterns = [
    path("", ListProject.as_view()),
    path("<id>", RetrieveProject.as_view())
]
