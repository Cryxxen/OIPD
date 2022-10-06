from rest_framework.routers import DefaultRouter

from apps.libraries.views import RussianLibraryApiViewSet, EnglishLibraryApiViewSet


router = DefaultRouter()
router.register(
    prefix='language/en',
    viewset=EnglishLibraryApiViewSet
)
router.register(
    prefix='language/ru',
    viewset=RussianLibraryApiViewSet
)

urlpatterns = router.urls
