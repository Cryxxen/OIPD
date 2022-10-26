from django.contrib import admin

from apps.about_us.models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text_ru',
        'text_en',
        'image',
    )
