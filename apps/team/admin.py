from django.contrib import admin

from apps.team.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'fullname',
        'image'
    )
    list_filter = (
        'id',
        'language',
        'fullname',
    )
    search_fields = (
        'id',
        'language',
        'fullname',
    )
