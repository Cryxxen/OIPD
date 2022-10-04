from rest_framework.routers import DefaultRouter

from apps.socials.views import SocialApiViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=SocialApiViewSet
)
urlpatterns = router.urls
