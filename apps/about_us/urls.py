from django.urls import path

from apps.about_us import views


urlpatterns = [
    path("us/", views.AboutUsApiView.as_view()),
    path("partners/", views.AboutPartnersApiViewSet.as_view()),
    path("team/", views.AboutTeamApiViewSet.as_view())
]
