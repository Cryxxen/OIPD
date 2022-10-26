from django.contrib import admin

from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "title_ru",
        "create_at",
    )
    search_fields = (
        'title_ru',
        'title_en',

        'beneficiaries_ru',
        'beneficiaries_en',

        'description_ru',
        'description_en',

        'duration_ru',
        'duration_en',

        'location_ru',
        'location_en',

        'participants_ru',
        'participants_en',

        "create_at",
    )

    list_filter = (
        "id",
        'title_ru',
        'title_en',

        'beneficiaries_ru',
        'beneficiaries_en',

        'description_ru',
        'description_en',

        'duration_ru',
        'duration_en',

        'location_ru',
        'location_en',

        'participants_ru',
        'participants_en',

        "create_at",
    )
