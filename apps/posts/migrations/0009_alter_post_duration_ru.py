# Generated by Django 4.1.1 on 2022-11-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_posttype_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='duration_ru',
            field=models.CharField(max_length=256, verbose_name='duration russian'),
        ),
    ]
