from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from apps.categories.managers import CategoryManager


class Category(MPTTModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
        unique=True
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name='subcategory',
        blank=True, null=True
    )
    ordering = models.PositiveSmallIntegerField()

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Navbar'
        verbose_name_plural = 'Navbar'
        ordering = ("ordering",)

    def __str__(self):
        return f"{self.id} --- {self.title}"
