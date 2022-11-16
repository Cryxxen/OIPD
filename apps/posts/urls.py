from django.urls import path

from apps.posts.views import ListPost, RetrievePost, ListPostType


urlpatterns = [
    path("", ListPost.as_view()),
    path("post/<id>", RetrievePost.as_view()),
    path("types/", ListPostType.as_view()),
]
