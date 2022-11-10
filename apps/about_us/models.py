from django.db import models
from utils.models import BaseModel


class AboutUs(BaseModel):
    class TypeChoice(models.TextChoices):
        our_mission = "our_mission"
        about_us = "about_Us"

    type = models.CharField(
        max_length=256,
        choices=TypeChoice.choices,
        verbose_name="type"
    )
    title_ru = None
    title_en = None

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if AboutUs.objects.filter(type=self.type).count() < 1:
            return super().save(*args, **kwargs)
