from django.urls import path

from apps.libraries.views import RetrieveLibraryApiView, ListLibraryAPiView


urlpatterns = [
    path("<id>", RetrieveLibraryApiView.as_view()),
    path("", ListLibraryAPiView.as_view())
]
