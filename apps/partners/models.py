from django.db import models

from utils.models import BaseModel


class Partner(BaseModel):
    link = models.URLField(
        verbose_name='web-site'
    )
    description_ru = None
    description_en = None

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"
