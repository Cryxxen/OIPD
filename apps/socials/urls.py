from django.urls import path
from apps.socials.views import ListSocialApi


urlpatterns = [
    path("", ListSocialApi.as_view())
]
