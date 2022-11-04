from django.db import models

from utils.models import BaseModel


class OurApproach(BaseModel):
    image = models.ImageField(
        verbose_name='image'
    )
    numbers = models.PositiveIntegerField(
        verbose_name="projects count"
    )

    title_en = None
    title_ru = None

    class Meta:
        verbose_name = 'Наш подход'
        verbose_name_plural = 'Наш подход'
        ordering = ('id',)

    def __str__(self):
        return f"{self.id}"
