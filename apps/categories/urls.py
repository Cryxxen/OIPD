from rest_framework.routers import DefaultRouter

from apps.categories.views import EnglishCategoryApiViewSet, RussianCategoryApiViewSet


router = DefaultRouter()
router.register(
    prefix='language/en',
    viewset=EnglishCategoryApiViewSet
)
router.register(
    prefix='language/ru',
    viewset=RussianCategoryApiViewSet
)

urlpatterns = router.urls
