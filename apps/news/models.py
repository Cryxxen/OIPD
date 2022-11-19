from django.db import models

from utils.models import BaseModel


class New(BaseModel):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}---{self.title_ru}"


class NewSocial(models.Model):
    new = models.ForeignKey(
        New,
        on_delete=models.CASCADE,
        related_name="new_socials"
    )

    class SocialTypeChoice(models.TextChoices):
        FACEBOOK = "facebook"
        INSTAGRAM = "instagram"

    social = models.CharField(
        max_length=256,
        choices=SocialTypeChoice.choices,
        verbose_name="Социальная сеть"
    )
    link = models.URLField(
        verbose_name="ссылка на статью"
    )

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if NewSocial.objects.filter(social=self.social, new=self.new).all().count() < 2:
            return super().save(*args, **kwargs)
