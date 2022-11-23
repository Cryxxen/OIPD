from django.db import models

from apps.posts.models import PostType
from utils.models import BaseModel


class ServiceText(BaseModel):
    type = models.ForeignKey(
        PostType,
        on_delete=models.CASCADE,
        verbose_name="service type"
    )

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return self.title_ru

    def save(self, *args, **kwargs):
        if ServiceText.objects.filter(type=self.type).count() < 1:
            return super().save(*args, **kwargs)
