from django.db import models

from apps.categories.models import Category


class AboutUs(models.Model):
    class LanguageChoice(models.TextChoices):
        ENGLISH = 'english'
        RUSSIAN = 'russian'

    language = models.CharField(
        max_length=256,
        choices=LanguageChoice.choices
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=256

    )
    subtitle = models.CharField(
        verbose_name='О нас',
        default='О нас',
        max_length=256,
    )
    text = models.TextField(
        verbose_name="О нас"
    )
    image = models.ImageField(
        verbose_name="Картинка"
    )

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"
