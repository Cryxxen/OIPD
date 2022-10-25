from django.db import models

from utils.models import BaseModel


class Club(BaseModel):
    image = models.ImageField(
        verbose_name='фотография'
    )
    title = models.CharField(
        max_length=256,
        verbose_name="Названии"
    )

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы мира"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.language}---{self.title}"
