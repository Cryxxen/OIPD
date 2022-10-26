from django.db import models

from utils.models import BaseModel


class Project(BaseModel):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"
