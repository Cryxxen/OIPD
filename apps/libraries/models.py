from django.db import models

from utils.models import BaseModel


class Library(BaseModel):
    image = models.ImageField(
        verbose_name='Обложка'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    link = models.URLField(
        verbose_name='Ссылка'
    )

    class Meta:
        verbose_name = 'Библиотеки'
        verbose_name_plural = 'Библиотека'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.id} --- {self.language} --- {self.title}"
