# Generated by Django 4.1.1 on 2022-10-25 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_options_project_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='instagram_link',
        ),
    ]
