from django.db import models

from utils.models import BaseModel


class Category(BaseModel):
    is_active = models.BooleanField(
        default=True,
        verbose_name='Показывать на сайте или нет'
    )
    ordering = models.PositiveSmallIntegerField()
    route = models.CharField(
        max_length=256,
        verbose_name="endpoint на который должна перекидывать"
    )

    description_en = None
    description_ru = None
    image = None

    class Meta:
        verbose_name = 'Разделы'
        verbose_name_plural = 'Раздел'
        ordering = ("ordering",)

    def __str__(self):
        return f"{self.id}"
