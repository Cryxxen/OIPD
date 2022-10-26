from rest_framework import generics

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.viewable().all()
    serializer_class = CategorySerializer
