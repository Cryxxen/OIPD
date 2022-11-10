from django.urls import path

from apps.contacts.views import ContactUsApiView, BidApiView


urlpatterns = [
    path("", ContactUsApiView.as_view()),
    path("bid/", BidApiView.as_view())
]
