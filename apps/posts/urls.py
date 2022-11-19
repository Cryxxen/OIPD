from rest_framework.routers import DefaultRouter

from apps.posts.views import PostApiViewSet, ListPostType

router = DefaultRouter()
router.register(
    prefix="posts",
    viewset=PostApiViewSet
)
router.register(
    prefix="types",
    viewset=ListPostType
)

urlpatterns = router.urls
