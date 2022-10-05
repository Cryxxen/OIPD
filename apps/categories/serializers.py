from rest_framework import serializers

from apps.categories.models import Category


class RecursionData(serializers.ModelSerializer):
    class Meta:

        def to_representation(self, value):
            serializer = self.parent.parent.__class__(value, context=self.context)
            return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    subcategory = RecursionData(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'subcategory',
            'ordering',
        )
