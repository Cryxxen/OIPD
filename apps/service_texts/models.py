from django.db import models

from utils.models import BaseModel


class ServiceText(BaseModel):
    class ServiceTypeChoice(models.TextChoices):
        library = "library"
        simulation_game = "Simulation game"
        projects = "Projects"
        training = "Training"
        club = "Club"

    type = models.CharField(
        max_length=256,
        choices=ServiceTypeChoice.choices,
        verbose_name="service type"
    )

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return self.title_ru

    def save(self, *args, **kwargs):
        if ServiceText.objects.filter(type=self.type).count() < 1:
            return super().save(*args, **kwargs)
