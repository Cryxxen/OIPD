from django.contrib import admin

from apps.news.models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title_ru',
        'title_en',
        'create_at',
    )
    search_fields = (
        'id',
        'title_ru',
        'title_en',
        'create_at',
    )
    list_filter = (
        'id',
        'title_ru',
        'title_en',
        'create_at',
    )
