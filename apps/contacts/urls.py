from django.urls import path

from apps.contacts.views import ContactUsApiView


urlpatterns = [
    path("", ContactUsApiView.as_view())
]
