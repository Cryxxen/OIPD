from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ClubRussianApiView, ClubEnglishApiView

urlpatterns = [
    path("ru/", ClubRussianApiView.as_view()),
    path("en/", ClubEnglishApiView.as_view()),
]
