from django.db import models

from utils.models import BaseModel


class Project(BaseModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    # instagram_link = models.URLField(
    #     verbose_name='ссылка на инстаграмм пост',
    #     blank=True
    # )
    #
    # facebook_link = models.URLField(
    #     verbose_name='Ссылка на фейсбук пост'
    # )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} --- {self.language} --- {self.title}"
