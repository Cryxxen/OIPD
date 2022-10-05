from rest_framework import serializers

from apps.libraries.models import Library


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"
