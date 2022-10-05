from django.contrib import admin

from apps.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'ordering',
        'title',
        'parent',
    )
    search_fields = (
        'id',
        'language',
        'ordering',
        'title',
        'parent',
    )
    list_filter = (
        'id',
        'ordering',
        'language',
        'title',
    )
