from django.contrib import admin

from apps.contacts.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'address',
        'email',
        'phone_number'
    )
