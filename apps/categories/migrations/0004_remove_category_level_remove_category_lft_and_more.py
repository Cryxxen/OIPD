# Generated by Django 4.1.1 on 2022-10-26 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_remove_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='level',
        ),
        migrations.RemoveField(
            model_name='category',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tree_id',
        ),
    ]