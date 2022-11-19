from django.db import models

from utils.models import BaseModel


class PostType(BaseModel):
    description_en = None
    description_ru = None
    image = None
    value = models.CharField(
        max_length=256,
        verbose_name="Значение"
    )

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = "Тип поста"
        verbose_name_plural = "Типы постов"


class Post(BaseModel):
    post_type = models.ForeignKey(
        PostType,
        on_delete=models.CASCADE,
        related_name="post_type",
        verbose_name="post type"
    )

    beneficiaries = models.PositiveSmallIntegerField(
        verbose_name="beneficiaries english"
    )

    # russian version 👇
    duration_ru = models.CharField(
        max_length=256,
        verbose_name="duration russian"
    )
    location_ru = models.CharField(
        max_length=256,
        verbose_name="location russian"
    )

    participants_ru = models.CharField(
        max_length=256,
        verbose_name="participants russian"
    )

    #  english version 👇

    duration_en = models.CharField(
        max_length=256,
        verbose_name="duration english"
    )
    location_en = models.CharField(
        max_length=256,
        verbose_name="location english"
    )
    participants_en = models.CharField(
        max_length=256,
        verbose_name="participants english"
    )
    target_audience_ru = models.CharField(
        max_length=256,
        verbose_name="Target audience russian"
    )
    target_audience_en = models.CharField(
        max_length=256,
        verbose_name="Target audience english"
    )
    project_goals_ru = models.TextField(
        verbose_name="Project goals russian"
    )
    project_goals_en = models.TextField(
        verbose_name="Project goals english"
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"
        ordering = ("-create_at",)

    def __str__(self):
        return f"{self.id}--{self.create_at}"


class PostSocial(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="post_socials"
    )

    class SocialTypeChoice(models.TextChoices):
        FACEBOOK = "facebook"
        INSTAGRAM = "instagram"
        YOUTUBE = "youtube"

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
        if PostSocial.objects.filter(social=self.social, post_id=self.post.id).count() < 1:
            return super().save(*args, **kwargs)
