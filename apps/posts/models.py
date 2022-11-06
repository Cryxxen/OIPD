from django.db import models

from utils.models import BaseModel


class PostType(BaseModel):
    description_en = None
    description_ru = None
    image = None

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = "Тип поста"
        verbose_name_plural = "Типы постов"


class Post(BaseModel):
    post_type = models.ForeignKey(
        PostType,
        on_delete=models.CASCADE,
        related_name="post_type",
        verbose_name="post type"
    )

    beneficiaries = models.PositiveSmallIntegerField(
        verbose_name="beneficiaries english"
    )

    # russian version 👇
    duration_ru = models.CharField(
        max_length=256,
        verbose_name="duration"
    )
    location_ru = models.CharField(
        max_length=256,
        verbose_name="location russian"
    )
    participants_ru = models.CharField(
        max_length=256,
        verbose_name="participants russian"
    )

    #  english version 👇

    duration_en = models.CharField(
        max_length=256,
        verbose_name="duration english"
    )
    location_en = models.CharField(
        max_length=256,
        verbose_name="location english"
    )
    participants_en = models.CharField(
        max_length=256,
        verbose_name="participants english"
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"
        ordering = ("-create_at",)

    def __str__(self):
        return f"{self.id}--{self.create_at}"
