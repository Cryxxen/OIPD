from django.db import models


class OurApproach(models.Model):
    class LanguageChoice(models.TextChoices):
        ENGLISH = 'english'
        RUSSIAN = 'russian'

    language = models.CharField(
        max_length=256,
        choices=LanguageChoice.choices
    )

    image = models.ImageField(
        verbose_name='Обложка'
    )

    text = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Наш подход'
        verbose_name_plural = 'Наш подход'
        ordering = ('id',)

    def __str__(self):
        return f"{self.id} -- {self.text}"
