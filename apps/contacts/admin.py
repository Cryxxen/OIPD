from django.contrib import admin

from apps.contacts.models import ContactUs, Bid


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'address_ru',
        'address_en',
        'email',
        'phone_number'
    )


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "surname",
        "description",
        "created_at",
    )
