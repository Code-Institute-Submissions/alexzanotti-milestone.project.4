# Generated by Django 3.2.19 on 2023-05-12 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_alter_category_options'),
        ('checkout', '0004_auto_20230512_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='full_name',
            new_name='user_name',
        ),
        migrations.DeleteModel(
            name='OrderLineItem',
        ),
        migrations.AddField(
            model_name='planorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order'),
        ),
        migrations.AddField(
            model_name='planorder',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.plan'),
        ),
    ]
