# Generated by Django 4.1.1 on 2022-11-05 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='new',
            name='twitter',
        ),
        migrations.CreateModel(
            name='NewSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social', models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram')], max_length=256, verbose_name='Социальная сеть')),
                ('link', models.URLField(verbose_name='ссылка на статью')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='news.new')),
            ],
        ),
    ]
