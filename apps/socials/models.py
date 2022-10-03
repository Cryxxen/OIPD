from django.db import models


class Contact(models.Model):
    meta = models.URLField(
        verbose_name='Facebook'
    )
    twitter = models.URLField(
        verbose_name='Twitter'
    )
    instagram = models.URLField(
        verbose_name='Instagram'
    )
    youtube = models.URLField(
        verbose_name='Youtube'
    )

    class Meta:
        verbose_name = "Социальные сети"
        verbose_name_plural = "Социальные сети"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.phone_number} --- {self.street}"
