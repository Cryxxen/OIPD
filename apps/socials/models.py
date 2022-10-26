from django.db import models

from utils.models import BaseModel


class Social(models.Model):
    icon = models.ImageField(
        verbose_name='logo image'
    )
    link = models.URLField(
        verbose_name='link'
    )

    class Meta:
        verbose_name = "Социальные сети"
        verbose_name_plural = "Социальные сети"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"
