# Generated by Django 5.1.3 on 2024-11-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_rename_photo_customer_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
