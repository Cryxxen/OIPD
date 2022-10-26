from django.contrib import admin

from apps.partners.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title_ru',
        'title_en'
    )
    search_fields = (
        'id',
        'title_en'
        'title_ru'
    )

