from rest_framework.routers import DefaultRouter

from apps.news.views import (
    EnglishNewApiViewSet,
    RussianNewApiViewSet
)

router = DefaultRouter()
router.register(
    prefix='language/en',
    viewset=EnglishNewApiViewSet
)
router.register(
    prefix='language/ru',
    viewset=RussianNewApiViewSet
)

urlpatterns = router.urls
