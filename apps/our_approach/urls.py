from django.urls import path

from apps.our_approach.views import ListAPIView, RetrieveAPIView

urlpatterns = [
    path("", ListAPIView.as_view()),
    path("<id>", RetrieveAPIView.as_view())
]
