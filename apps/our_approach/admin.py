from django.contrib import admin

from apps.our_approach.models import OurApproach


@admin.register(OurApproach)
class OurApproachAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description_ru',
        'description_en',
        'image',
    )
    search_fields = (
        'id',
        'description_ru',
        'description_en',
        'create_at',
    )
    list_filter = (
        'id',
        'description_ru',
        'description_en',
    )
