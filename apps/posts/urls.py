from django.urls import path

from apps.posts.views import ListGame, RetrieveGame


urlpatterns = [
    path("", ListGame.as_view()),
    path("<id>", RetrieveGame.as_view())
]
