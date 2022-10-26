from django.db import models

from utils.models import BaseModel


class Club(models.Model):
    image = models.ImageField(
        verbose_name='фотография'
    )
    title_ru = models.CharField(
        max_length=256,
        verbose_name="Названии"
    )
    title_en = models.CharField(
        max_length=256,
        verbose_name="title"
    )

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы мира"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}---{self.title_ru}"
