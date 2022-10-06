# Generated by Django 4.1.1 on 2022-10-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('language', models.CharField(choices=[('english', 'English'), ('russian', 'Russian')], max_length=256)),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('fullname', models.CharField(max_length=256, verbose_name='ФИО')),
                ('position', models.CharField(max_length=256, verbose_name='Должность')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('facebook', models.URLField(verbose_name='Ссылка на профиль(facebook)')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команда',
                'ordering': ('-id',),
            },
        ),
    ]