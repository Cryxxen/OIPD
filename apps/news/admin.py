from django.contrib import admin

from apps.news.models import New, NewSocial


class NewSocialInline(admin.TabularInline):
    model = NewSocial
    extra = 0
    max_num = 2


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    inlines = [
        NewSocialInline
    ]
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
