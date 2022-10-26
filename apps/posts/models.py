from django.db import models

from utils.models import BaseModel


class Post(BaseModel):
    class PostTypeChoice(models.TextChoices):
        simulation_game = "SIMULATION GAME"
        project = "PROJECT"
        digital_solution = "DIGITAL SOLUTIONS"
        trainings = "TRAININGS"

    post_type = models.CharField(
        choices=PostTypeChoice.choices,
        max_length=256
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
