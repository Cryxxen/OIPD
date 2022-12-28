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

class AboutPartners(models.Model):
    content_ru = models.TextField()
    content_en = models.TextField()

    def __str__(self):
        return self.content_ru

    def save(self, *args, **kwargs):
        if AboutPartners.objects.all().count() >= 1:
           return None
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "О партнере"
        verbose_name_plural = "О партнерах"


class AboutTeam(models.Model):
    content_ru = models.TextField()
    content_en = models.TextField()

    def __str__(self):
        return self.content_ru

    def save(self, *args, **kwargs):
        if AboutTeam.objects.all().count() >= 1:
           return None
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "О команде"
        verbose_name_plural = "О команде"
