from rest_framework.routers import DefaultRouter

from apps.about_us.views import EnglishAboutUsApiViewSet, RussianAboutUsApiViewSet


router = DefaultRouter()
router.register(
    prefix='language/en',
    viewset=EnglishAboutUsApiViewSet
)
router.register(
    prefix='language/ru',
    viewset=RussianAboutUsApiViewSet
)

urlpatterns = router.urls
