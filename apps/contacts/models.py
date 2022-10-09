from django.db import models

from utils.models import BaseModel


class ContactUs(BaseModel):
    country = models.CharField(
        max_length=256,
        verbose_name="Кыргызская Республика",
        default='Кыргызская Республика'
    )
    some_numbers = models.PositiveIntegerField(
        verbose_name='720021'
    )
    city = models.CharField(
        max_length=256,
        verbose_name='Город',
        default='г.'
    )
    street = models.CharField(
        max_length=256,
        verbose_name='Улица',
    )
    town = models.CharField(
        max_length=256,
        verbose_name='Здание'
    )
    at_foot = models.PositiveSmallIntegerField(
        verbose_name='Этаж'
    )
    entrance = models.CharField(
        max_length=256,
        verbose_name='Вход со стороны?'
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
