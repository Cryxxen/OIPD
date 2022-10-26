from django.db import models


class BaseModel(models.Model):
    image = models.ImageField(
        verbose_name='Обложка'
    )
    title_ru = models.CharField(
        max_length=256,
        verbose_name='title russian'
    )
    title_en = models.CharField(
        max_length=256,
        verbose_name='title english'
    )

    description_ru = models.TextField(
        verbose_name='description russian'
    )
    description_en = models.TextField(
        verbose_name='description english'
    )

    create_at = models.DateField(
        verbose_name='created data',
        auto_now_add=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.id}"
