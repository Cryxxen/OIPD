from django.db import models

from utils.models import BaseModel


class AboutUs(BaseModel):
    title = models.CharField(
        verbose_name='Название',
        max_length=256
    )
    image = models.ImageField(
        verbose_name="Картинка"
    )
    text = models.TextField(
        verbose_name="О нас"
    )

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if AboutUs.objects.all().count() == 4:
            return None
        else:
            super().save(*args, **kwargs)
