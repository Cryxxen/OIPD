from django.urls import path

from .views import ListClubApiView, RetrieveClubAPIView

urlpatterns = [
    path("", ListClubApiView.as_view()),
    path("<id>", RetrieveClubAPIView.as_view()),
]
