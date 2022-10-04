from rest_framework.routers import DefaultRouter

from apps.contacts.views import ContactUsApiViewSet


router = DefaultRouter()
router.register(
    prefix='',
    viewset=ContactUsApiViewSet
)

urlpatterns = router.urls
