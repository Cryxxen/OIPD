# Generated by Django 4.1.1 on 2022-10-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options_category_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='language',
            field=models.CharField(choices=[('english', 'English'), ('russian', 'Russian')], max_length=256),
        ),
    ]