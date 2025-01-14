# Generated by Django 5.1.3 on 2024-11-27 07:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_orderrecords_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrecords',
            name='final_price',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
        migrations.AddField(
            model_name='orderrecords',
            name='number',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
