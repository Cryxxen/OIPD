from django.db import models


class BaseModel(models.Model):
    class LanguageChoice(models.TextChoices):
        ENGLISH = 'english'
        RUSSIAN = 'russian'

    create_at = models.DateField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    language = models.CharField(
        max_length=256,
        choices=LanguageChoice.choices
    )

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} --- {self.language}"
    