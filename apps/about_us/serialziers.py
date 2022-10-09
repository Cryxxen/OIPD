from rest_framework import serializers

from apps.about_us.models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"

    # def create(self, validated_data):
    #     queryset_len = AboutUs.objects.all().count()
    #     if queryset_len == 2:
    #         raise "You cannot create more than 3 entries"
    #     else:
    #         if self.save()
