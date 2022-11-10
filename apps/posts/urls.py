from django.urls import path

from apps.posts.views import ListPost, RetrievePost


urlpatterns = [
    path("", ListPost.as_view()),
    path("<id>", RetrievePost.as_view())
]
