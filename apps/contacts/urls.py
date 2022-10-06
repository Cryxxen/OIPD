from rest_framework.routers import DefaultRouter

from apps.contacts.views import EnglishContactUsApiViewSet, RussianContactUsApiViewSet


router = DefaultRouter()
router.register(
    prefix='language/en',
    viewset=EnglishContactUsApiViewSet
)
router.register(
    prefix='language/ru',
    viewset=RussianContactUsApiViewSet
)

urlpatterns = router.urls
