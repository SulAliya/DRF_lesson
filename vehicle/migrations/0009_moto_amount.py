# Generated by Django 4.2.14 on 2024-08-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_car_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='amount',
            field=models.IntegerField(default=1000, verbose_name='цена'),
        ),
    ]
