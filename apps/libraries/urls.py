from rest_framework.routers import DefaultRouter

from apps.libraries.views import RetrieveLibraryApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=RetrieveLibraryApiViewSet,
)

urlpatterns = router.urls

