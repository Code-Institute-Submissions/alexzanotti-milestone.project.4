# Generated by Django 3.2.19 on 2023-05-20 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_donated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='donated',
        ),
    ]