from django.db import models

from utils.models import BaseModel


class Library(BaseModel):

    link = models.URLField(
        verbose_name='link to google drive'
    )

    description_ru = None
    description_en = None

    class Meta:
        verbose_name = 'Библиотеки'
        verbose_name_plural = 'Библиотека'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.id}"
