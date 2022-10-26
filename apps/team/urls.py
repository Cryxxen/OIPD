from django.urls import path

from apps.team.views import RetrieveTeam, ListTeam

urlpatterns = [
    path("", ListTeam.as_view()),
    path("<id>", RetrieveTeam.as_view())
]
