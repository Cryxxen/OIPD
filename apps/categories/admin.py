from django.contrib import admin

from apps.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title_ru',
        'title_en',
        'ordering',
        'is_active',
    )
    search_fields = (
        'id',
        'title_ru',
        'title_en',
        'ordering',
        'is_active',
    )
    list_filter = (
        'id',
        'title_ru',
        'title_en',
        'ordering',
        'is_active',
    )
