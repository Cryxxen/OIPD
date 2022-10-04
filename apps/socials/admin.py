from django.contrib import admin

from apps.socials.models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'instagram'
    )
    search_fields = (
        'id',
        'city',
        'phone_number',
    )
