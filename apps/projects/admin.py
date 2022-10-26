from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title_ru',
        'title_en',
    )
    search_fields = (
        "id",
        "title_ru",
        "title_en",
        "description_en",
        "description_en",
    )
    list_filter = (
        "title_ru",
        "title_en",
        "description_en",
        "description_en",
    )
