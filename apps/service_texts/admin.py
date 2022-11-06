from django.contrib import admin

from apps.service_texts.models import ServiceText


@admin.register(ServiceText)
class ServiceTextAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
        "title_ru",
        "title_en",
        "description_ru",
        "description_en",
        "image",
    )