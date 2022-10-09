from django.contrib import admin

from apps.about_us.models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'title',
        'image',
    )
    search_fields = (
        'id',
        'title',
        'text'
    )
