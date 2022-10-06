from rest_framework.routers import DefaultRouter

from apps.partners.views import EnglishPartnerApiViewSet, RussianPartnerApiViewSet

router = DefaultRouter()
router.register(
    prefix='language/en',
    viewset=EnglishPartnerApiViewSet
)
router.register(
    prefix='language/ru',
    viewset=RussianPartnerApiViewSet
)

urlpatterns = router.urls
