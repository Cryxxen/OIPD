from django.contrib import admin

from apps.contacts.models import ContactUs, Bid, PhoneNumber


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    inlines = [
        PhoneNumberInline
    ]
    list_display = (
        'id',
        'address_ru',
        'address_en',
        'email',
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
