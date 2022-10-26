from django.urls import path

from apps.partners.views import RetrievePartner, ListPartner

urlpatterns = [
    path("", ListPartner.as_view()),
    path("<id>", RetrievePartner.as_view())
]
