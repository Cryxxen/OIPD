from django.db import models

from utils.models import BaseModel


class New(BaseModel):
    image = models.ImageField(
        verbose_name='Обложка'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    facebook = models.URLField(
        verbose_name='Ссылка на пост в фейсбуке'
    )
    twitter = models.URLField(
        verbose_name='Ссылка на пост в твиттере'
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.language}---{self.title}"


# class NewImage(models.Model):
#     new = models.ForeignKey(
#         New,
#         related_name='images',
#         verbose_name='новость',
#         on_delete=models.CASCADE,
#     )
#     image = models.ImageField(
#         verbose_name='Изображение'
#     )
#
#     class Meta:
#         verbose_name = 'New Image'
#         verbose_name_plural = 'New Images'
#         ordering = ('-id',)
#
#     def __str__(self):
#         return f"{self.new.title}"
