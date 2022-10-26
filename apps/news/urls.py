from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.news.views import (
    ListNewApiView,
    RetrieveNewApiView
)

urlpatterns = [
    path("", ListNewApiView.as_view()),
    path("<id>", RetrieveNewApiView.as_view())
]
