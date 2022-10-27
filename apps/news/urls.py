from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.news.views import (
    RetrieveNewApiViewSet
)
router = DefaultRouter()
router.register(
    prefix="",
    viewset=RetrieveNewApiViewSet
)
urlpatterns = router.urls
