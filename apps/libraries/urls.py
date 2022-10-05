from rest_framework.routers import DefaultRouter

from apps.libraries.views import LibraryApiViewSet


router = DefaultRouter()
router.register(
    prefix='',
    viewset=LibraryApiViewSet
)

urlpatterns = router.urls
