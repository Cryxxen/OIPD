from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    create_at = models.DateField(
        auto_now_add=True
    )

    instagram_link = models.URLField(
        verbose_name='ссылка на инстаграмм пост'
    )

    facebook_link = models.URLField(
        verbose_name='Ссылка на фейсбук пост'
    )
