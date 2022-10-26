from django.contrib import admin

from apps.team.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fullname_ru',
        'fullname_en',
        'image'
    )
    list_filter = (
        'id',
        'fullname_ru',
        'fullname_en',
    )
    search_fields = (
        'id',
        'fullname_ru',
        'fullname_en',
    )
