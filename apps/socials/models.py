from django.db import models


class Social(models.Model):
    icon = models.ImageField(
        verbose_name='Facebook'
    )
    link = models.URLField(
        verbose_name='Twitter'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Instagram'
    )

    class Meta:
        verbose_name = "Социальные сети"
        verbose_name_plural = "Социальные сети"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.title}"
