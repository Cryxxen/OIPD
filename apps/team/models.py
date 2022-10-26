from django.db import models

from utils.models import BaseModel


class Team(models.Model):
    image = models.ImageField(
        verbose_name='image'
    )
    fullname_ru = models.CharField(
        max_length=256,
        verbose_name='fullname russian'
    )
    position_ru = models.CharField(
        max_length=256,
        verbose_name='position russian'
    )

    fullname_en = models.CharField(
        max_length=256,
        verbose_name="fullname english"
    )
    position_en = models.CharField(
        max_length=256,
        verbose_name="position english"
    )
    email = models.EmailField(
        verbose_name='email'
    )
    facebook = models.URLField(
        verbose_name='link facebook account'
    )

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} --- {self.fullname_ru} --- {self.fullname_en}"
