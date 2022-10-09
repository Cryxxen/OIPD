from django.db import models

from utils.models import BaseModel


class OurApproach(BaseModel):
    image = models.ImageField(
        verbose_name='Обложка'
    )

    text = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Наш подход'
        verbose_name_plural = 'Наш подход'
        ordering = ('id',)

    def __str__(self):
        return f"{self.id} --- {self.language} --- {self.text}"
