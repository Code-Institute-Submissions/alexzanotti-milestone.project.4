# Generated by Django 3.2.19 on 2023-05-15 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_remove_plan_image_urlfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='price',
        ),
    ]
