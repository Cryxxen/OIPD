from django.db import models

from utils.models import BaseModel


class ContactUs(models.Model):
    address = models.CharField(
        max_length=256,
        verbose_name='Адрес',
        default="21/2 Tokombaev str, Bishkek 720000, Kyrgyzstan"
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
        if ContactUs.objects.all() < 1:
            super().save(*args, **kwargs)
        else:
            return None
