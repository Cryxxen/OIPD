# Generated by Django 4.1.1 on 2022-11-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_approach', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourapproach',
            name='numbers',
            field=models.PositiveIntegerField(default=1, verbose_name='projects count'),
            preserve_default=False,
        ),
    ]
