from django.db import models


class Social(models.Model):
    icon = models.ImageField(
        verbose_name='Логотип'
    )
    link = models.URLField(
        verbose_name='Ссылка'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Название соц. сети'
    )

    class Meta:
        verbose_name = "Социальные сети"
        verbose_name_plural = "Социальные сети"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.title}"
