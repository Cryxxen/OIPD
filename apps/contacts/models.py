from django.db import models

from utils.validators import phone_validator


class ContactUs(models.Model):
    address_ru = models.CharField(
        max_length=256,
        verbose_name='Адрес',
        default="Адрес: ул. Токомбаева 21/2, Бишкек 720000, Кыргызстан "
    )
    address_en = models.CharField(
        max_length=256,
        verbose_name='Адрес',
        default="Address: 21/2 Tokombaev str, Bishkek 720000, Kyrgyzstan "
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name='phone number'
    )
    email = models.EmailField(
        verbose_name='email'
    )

    class Meta:
        verbose_name = 'Наши Контакты'
        verbose_name_plural = 'Наши Контакты'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if ContactUs.objects.all().count() < 1:
            super().save(*args, **kwargs)
        else:
            return None


class Bid(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="name"
    )
    surname = models.CharField(
        max_length=256,
        verbose_name="surname"
    )
    phone_number = models.CharField(
        max_length=14,
        verbose_name="phone number",
        validators=[phone_validator]
    )
    description = models.TextField(
        verbose_name="Description"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=""
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.name}--{self.surname}"
