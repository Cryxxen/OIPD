from django.db import models

from utils.models import BaseModel


class AboutUs(BaseModel):
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
        elif AboutUs.objects.filter(language='russian').count() == 2 and self.language == 'russian':
            return None
        elif AboutUs.objects.filter(language='english').count() == 2 and self.language == 'english':
            return None
        else:
            super().save(*args, **kwargs)
