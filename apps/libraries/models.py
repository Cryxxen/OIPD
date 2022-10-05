from django.db import models


class Library(models.Model):
    image = models.FileField(
        verbose_name='Обложка'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    link = models.URLField(
        verbose_name='Ссылка'
    )

    class Meta:
        verbose_name = 'Библиотеки'
        verbose_name_plural = 'Библиотека'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.id} --- {self.title}"
