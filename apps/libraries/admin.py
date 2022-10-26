from django.contrib import admin

from apps.libraries.models import Library


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title_ru',
        'title_en',
        'link',
    )
    search_fields = (
        'id',
        'title_ru',
        'title_en',
        'link',
    )
    list_filter = (
        'id',
        "title_en",
        "title_ru",
    )
