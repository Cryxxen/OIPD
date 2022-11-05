from utils.models import BaseModel


class AboutUs(BaseModel):
    title_ru = None
    title_en = None

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
