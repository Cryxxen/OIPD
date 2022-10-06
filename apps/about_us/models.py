from django.db import models

from utils.models import BaseModel


class AboutUs(BaseModel):
    title = models.CharField(
        verbose_name='Название',
        max_length=256
    )
    subtitle = models.CharField(
        verbose_name='О нас',
        default='О нас',
        max_length=256,
    )
    text = models.TextField(
        verbose_name="О нас"
    )
    image = models.ImageField(
        verbose_name="Картинка"
    )

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"
