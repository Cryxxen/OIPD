from rest_framework import viewsets

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryApiViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.viewable()
    serializer_class = CategorySerializer
