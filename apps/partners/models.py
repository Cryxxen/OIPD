from django.db import models


class Partner(models.Model):
    logo = models.ImageField(
        verbose_name='Логотип партнера',
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Название компании'
    )

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} --- {self.title}"
