# Generated by Django 5.1.3 on 2024-11-26 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_customer_phone'),
        ('pizza', '0005_alter_pizza_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrecords',
            name='customer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='orderrecords',
            name='pizza_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.pizza'),
        ),
    ]