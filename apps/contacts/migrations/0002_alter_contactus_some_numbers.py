# Generated by Django 4.1.1 on 2022-10-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='some_numbers',
            field=models.PositiveIntegerField(verbose_name='какой-то код похожий на 720021'),
        ),
    ]
