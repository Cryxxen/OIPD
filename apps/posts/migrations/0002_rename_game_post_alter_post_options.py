# Generated by Django 4.1.1 on 2022-10-26 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Game',
            new_name='Post',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-create_at',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
