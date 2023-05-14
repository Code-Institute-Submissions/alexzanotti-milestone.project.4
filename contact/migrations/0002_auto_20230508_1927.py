# Generated by Django 3.2.19 on 2023-05-08 19:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Assigned', 'Assigned'), ('In Progress', 'In Progress'), ('Pending', 'Pending'), ('Resolved', 'Resolved')], default='New', max_length=20),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]