from rest_framework.routers import DefaultRouter

from apps.our_approach.views import EnglishOurApproachApiViewSet, RussianOurApproachApiViewSet

router = DefaultRouter()
router.register(
    prefix='en',
    viewset=EnglishOurApproachApiViewSet
)
router.register(
    prefix='ru',
    viewset=RussianOurApproachApiViewSet
)

urlpatterns = router.urls
