from rest_framework.routers import DefaultRouter

from apps.categories.views import EnglishCategoryApiViewSet, RussianCategoryApiViewSet


router = DefaultRouter()
router.register(
    prefix='en',
    viewset=EnglishCategoryApiViewSet
)
router.register(
    prefix='ru',
    viewset=RussianCategoryApiViewSet
)

urlpatterns = router.urls
