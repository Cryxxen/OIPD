from django.contrib import admin

from apps.our_approach.models import OurApproach


@admin.register(OurApproach)
class OurApproachAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
    )
    search_fields = (
        'id',
        'language',
        'text'
    )
    list_filter = (
        'id',
        'language',
        'text',
    )
