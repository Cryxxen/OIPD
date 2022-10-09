from django.contrib import admin

from apps.libraries.models import Library


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'title',
        'link',
    )
    search_fields = (
        'id',
        'title',
        'link',
    )
    list_filter = (
        'id',
        'language',
    )
