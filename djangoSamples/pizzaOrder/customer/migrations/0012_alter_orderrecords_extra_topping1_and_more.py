# Generated by Django 5.1.3 on 2024-11-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_alter_orderrecords_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrecords',
            name='extra_topping1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='orderrecords',
            name='extra_topping2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='orderrecords',
            name='other_wishes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
