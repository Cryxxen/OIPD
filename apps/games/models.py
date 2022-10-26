from django.db import models

from utils.models import BaseModel


class Game(BaseModel):
    # russian version 👇

    beneficiaries_ru = models.PositiveSmallIntegerField(
        verbose_name="beneficiaries russian",
    )
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
    beneficiaries_en = models.PositiveSmallIntegerField(
        verbose_name="beneficiaries english"
    )

    class Meta:
        verbose_name = 'Симуляционная игра'
        verbose_name_plural = "Симуляционные игры"
        ordering = ("-create_at",)

    def __str__(self):
        return f"{self.id}--{self.create_at}"
