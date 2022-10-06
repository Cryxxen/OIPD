from django.db import models

from utils.models import BaseModel


class Team(BaseModel):
    image = models.ImageField(
        verbose_name='Фотография'
    )
    fullname = models.CharField(
        max_length=256,
        verbose_name='ФИО'
    )
    position = models.CharField(
        max_length=256,
        verbose_name='Должность'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    facebook = models.URLField(
        verbose_name='Ссылка на профиль(facebook)'
    )

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} --- {self.language} --- {self.fullname}"
