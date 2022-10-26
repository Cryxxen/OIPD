from django.urls import path

from apps.about_us.views import AboutUsApiView


urlpatterns = [
    path("", AboutUsApiView.as_view())
]
