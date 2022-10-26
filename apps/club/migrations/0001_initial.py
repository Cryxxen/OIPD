# Generated by Django 4.1.1 on 2022-10-24 18:41

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
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('language', models.CharField(choices=[('english', 'English'), ('russian', 'Russian')], max_length=256)),
                ('image', models.ImageField(upload_to='', verbose_name='фотография')),
                ('title', models.CharField(max_length=256, verbose_name='Названии')),
            ],
            options={
                'verbose_name': 'Клуб',
                'verbose_name_plural': 'Клубы мира',
                'ordering': ('-id',),
            },
        ),
    ]