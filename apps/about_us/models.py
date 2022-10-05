from django.db import models


class AboutUs(models.Model):
    text = models.TextField(
        verbose_name="О нас"
    )
    image = models.ImageField(
        verbose_name="Картинка"
    )

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}"
