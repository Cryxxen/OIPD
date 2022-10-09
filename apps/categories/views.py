from rest_framework import viewsets

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class EnglishCategoryApiViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.viewable().filter(language='english', is_active=True).all()
    serializer_class = CategorySerializer


class RussianCategoryApiViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.viewable().filter(language='russian', is_active=True).all()
    serializer_class = CategorySerializer
