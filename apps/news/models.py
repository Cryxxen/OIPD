from django.db import models


class New(models.Model):
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
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    create_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.language}---{self.title}"


class NewImage(models.Model):
    new = models.ForeignKey(
        New,
        related_name='images',
        verbose_name='новость',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'New Image'
        verbose_name_plural = 'New Images'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.new.title}"
