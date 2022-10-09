from django.contrib import admin

from apps.partners.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'title'
    )
    search_fields = (
        'id',
        'title'
    )

