from django.db import models


class Library(models.Model):
    image = models.ImageField(
        verbose_name='Обложка'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    link = models.URLField(
        verbose_name='Ссылка'
    )

    def __str__(self):
        return f"{self.id} --- {self.title}"
