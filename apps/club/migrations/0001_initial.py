# Generated by Django 4.1.1 on 2022-10-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Обложка')),
                ('title_ru', models.CharField(max_length=256, verbose_name='title russian')),
                ('title_en', models.CharField(max_length=256, verbose_name='title english')),
                ('description_ru', models.TextField(verbose_name='description russian')),
                ('description_en', models.TextField(verbose_name='description english')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='created data')),
            ],
            options={
                'verbose_name': 'Клуб',
                'verbose_name_plural': 'Клубы мира',
                'ordering': ('-id',),
            },
        ),
    ]
