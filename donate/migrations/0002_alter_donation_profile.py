# Generated by Django 3.2.19 on 2023-05-20 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_donated'),
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
