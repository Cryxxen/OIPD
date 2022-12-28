from django.contrib import admin

from apps.about_us import models


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'description_ru',
        'description_en',
    )

@admin.register(models.AboutTeam)
class AboutTeamAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content_ru",
        "content_en",
    )


@admin.register(models.AboutPartners)
class AboutPartnersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content_ru",
        "content_en",
    )