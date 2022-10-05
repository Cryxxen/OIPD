from django.contrib import admin

from apps.socials.models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title'
    )
    search_fields = (
        'id',
        'link',
        'title',
    )
