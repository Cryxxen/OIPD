from django.db import models

from utils.models import BaseModel


class ContactUs(BaseModel):
    adsress = models.CharField(
        max_length=256,
        verbose_name='Адрес',
        default="21/2 Tokombaev str, Bishkek 720000, Kyrgyzstan"
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name='Тел'
    )
    email = models.EmailField(
        verbose_name='email'
    )

    class Meta:
        verbose_name = 'Наши Контакты'
        verbose_name_plural = 'Наши Контакты'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}---{self.language}"

    def save(self, *args, **kwargs):
        if ContactUs.objects.all().count() >= 2:
            return None
        elif ContactUs.objects.filter(language='english').count() >= 1 and self.language == 'english':
            return "Don't"
        elif ContactUs.objects.filter(language='russian').count() >= 1 and self.language == 'russian':
            return None
        else:
            super().save(*args, **kwargs)
