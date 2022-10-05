from rest_framework.routers import DefaultRouter

from apps.news.views import NewImageApiViewSet, NewApiViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=NewApiViewSet
)
router.register(
    prefix='images',
    viewset=NewImageApiViewSet
)

urlpatterns = router.urls
