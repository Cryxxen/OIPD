from django.db import models


class AboutUs(models.Model):
    image = models.ImageField(
        verbose_name="Картинка | Image"
    )
    text_ru = models.TextField(
        verbose_name="О нас"
    )
    text_en = models.TextField(
        verbose_name="about us"
    )

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if AboutUs.objects.all().count() < 1:
            super().save(*args, **kwargs)
        else:
            return None
