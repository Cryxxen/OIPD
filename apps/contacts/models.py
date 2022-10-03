from django.db import models


class ContactUs(models.Model):
    country = models.CharField(
        max_length=256,
        verbose_name="72300 Кыргызская Республика",
        default='72300 Кыргызская Республика'
    )
    city = models.CharField(
        max_length=256,
        verbose_name='Город',
        default='г.'
    )
    street = models.CharField(
        max_length=256,
        verbose_name='Улица',
    )
    town = models.CharField(
        max_length=256,
        verbose_name='Здание'
    )
    at_foot = models.PositiveSmallIntegerField(
        verbose_name='Этаж'
    )
    entrance = models.CharField(
        max_length=256,
        verbose_name='Вход со стороны?'
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name='Тел'
    )
    email = models.EmailField(
        verbose_name='email'
    )

    class Meta:
        verbose_name = 'Наши Контакты'
        verbose_name_plural = 'Наши Контакты'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.street}--{self.phone_number}"