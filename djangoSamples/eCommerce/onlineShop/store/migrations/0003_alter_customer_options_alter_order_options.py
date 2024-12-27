# Generated by Django 5.1.4 on 2024-12-23 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_customer_email_remove_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancle_order', 'can cancle an order')]},
        ),
    ]
