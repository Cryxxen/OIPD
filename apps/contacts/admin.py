from django.contrib import admin

from apps.contacts.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'email',
        'phone_number'
    )
    list_filter = (
        'id',
        'phone_number',
        'email',
    )
    search_fields = (
        'id',
        'city',
        'phone_number',
    )
