from django.db import models

from utils.models import BaseModel


class New(BaseModel):
    facebook = models.URLField(
        verbose_name='link facebook'
    )
    instagram = models.URLField(
        verbose_name='link to instagram'
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}---{self.title_ru }"


