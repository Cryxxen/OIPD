# Generated by Django 4.1.1 on 2022-10-05 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library',
            options={'ordering': ('-id',), 'verbose_name': 'Библиотеки', 'verbose_name_plural': 'Библиотека'},
        ),
    ]