from rest_framework.routers import DefaultRouter

from apps.our_approach.views import OurApproachViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=OurApproachViewSet
)
urlpatterns = router.urls
