from rest_framework.routers import DefaultRouter

from apps.service_texts.views import ServiceTextApiViewSet

router = DefaultRouter()
router.register(
    prefix="texts",
    viewset=ServiceTextApiViewSet
)

urlpatterns = router.urls
