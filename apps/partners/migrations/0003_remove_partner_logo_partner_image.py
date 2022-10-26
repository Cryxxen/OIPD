# Generated by Django 4.1.1 on 2022-10-26 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_remove_partner_image_partner_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='logo',
        ),
        migrations.AddField(
            model_name='partner',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Обложка'),
            preserve_default=False,
        ),
    ]
