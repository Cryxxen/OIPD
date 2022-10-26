from django.urls import path

from .views import ClubApiView

urlpatterns = [
    path("", ClubApiView.as_view()),
]
