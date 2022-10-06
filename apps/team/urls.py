from rest_framework.routers import DefaultRouter

from apps.team.views import EnglishTeamApiViewSet, RussianTeamApiViewSet

router = DefaultRouter()
router.register(
    prefix='en',
    viewset=EnglishTeamApiViewSet
)
router.register(
    prefix='ru',
    viewset=RussianTeamApiViewSet
)

urlpatterns = router.urls

