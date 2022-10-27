from rest_framework.routers import DefaultRouter

from apps.team.views import TeamApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=TeamApiViewSet
)
urlpatterns = router.urls
