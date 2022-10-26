from django.urls import path

from apps.categories.views import CategoryApiView


urlpatterns = [
    path("", CategoryApiView.as_view()),
]

