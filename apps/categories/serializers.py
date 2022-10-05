from rest_framework import serializers

from apps.categories.models import Category


class RecursiveData(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    subcategory = RecursiveData(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'language',
            'title',
            'subcategory',
            'ordering',
        )
