from rest_framework.routers import DefaultRouter

from apps.projects.views import RussianProjectApiViewSet, EnglishProjectApiViewSet


router = DefaultRouter()
router.register(
    prefix='en',
    viewset=EnglishProjectApiViewSet
)
router.register(
    prefix='ru',
    viewset=RussianProjectApiViewSet
)

urlpatterns = router.urls
