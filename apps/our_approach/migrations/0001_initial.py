# Generated by Django 4.1.1 on 2022-10-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurApproach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('language', models.CharField(choices=[('english', 'English'), ('russian', 'Russian')], max_length=256)),
                ('image', models.ImageField(upload_to='', verbose_name='Обложка')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Наш подход',
                'verbose_name_plural': 'Наш подход',
                'ordering': ('id',),
            },
        ),
    ]
