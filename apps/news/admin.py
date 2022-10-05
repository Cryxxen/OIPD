from django.contrib import admin

from apps.news.models import New, NewImage


class NewImageAdmin(admin.TabularInline,
                    admin.StackedInline):
    model = NewImage
    extra = 1


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'title',
        'create_at',
    )
    search_fields = (
        'id',
        'language',
        'title',
        'create_at',
        'description',
    )
    list_filter = (
        'id',
        'language',
        'create_at'
    )
    inlines = [NewImageAdmin]
